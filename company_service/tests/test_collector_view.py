from django.test import TestCase
from rest_framework.test import APIRequestFactory
from company_service import view as views
from users.models import User
from company_service.models import Company, Collector
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.tests.view_test_support import *
import json

class CollectorViewSetTest(TestCase):
    view = views.CollectorViewSet

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True, default_company=self.first_company)
        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd", is_active=False)

        self.first_collector = Collector.objects.create(company=self.first_company, mac="23123232", collector_type="Lora")
        self.second_collector = Collector.objects.create(company=self.first_company, mac="1223244", collector_type="HW")
        self.noise_collector = Collector.objects.create(company=self.noise_company, mac="", collector_type="collector-noise")
        
        self.first_company.users.add(self.active_user)
        self.noise_company.users.add(self.unactivated_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)

        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)
        self.authorization_active_token = 'Bearer {}'.format(self.active_token)

        self.index_route = '/v1/companies/{}/collectors'.format(self.first_company.id)
        self.single_route = '/v1/companies/{}/collectors/{}'.format(self.first_company.id, self.first_collector.id)
    
    def tearDown(self):
        self.first_company.delete()
        self.noise_company.delete()
        self.active_user.delete()
        self.unactivated_user.delete()
    
    def test_collector_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )
    
    def test_collector_list_authetication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.index_route,
            self.unactivated_token,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_collector_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_collector_list_response_is_200(self):
        collector_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = collector_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('UTF-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['mac'], self.second_collector.mac)
        self.assertEqual(response_dict['results'][1]['mac'], self.first_collector.mac)

    def test_collector_details_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.single_route,
            resource='retrieve',
            pk=self.first_collector.id,
            companies_pk=self.first_company.id
        )

    def test_collector_details_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.single_route,
            self.unactivated_token,
            resource='retrieve',
            pk=self.first_collector.id,
            companies_pk=self.first_company.id
        )
    
    def test_collector_details_response_is_404_when_collector_is_from_another_company(self):
        collector_view = self.view.as_view({'get':'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = collector_view(request, pk=self.noise_collector.id, companies_pk=self.noise_company.id)

        response.render()

        self.assertEqual(response.status_code, 404)

    def test_collector_details_response_is_200(self):
        collector_view = self.view.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = collector_view(request, pk=self.first_collector.id, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('UTF-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['id'], self.first_collector.id)
        self.assertEqual(response_dict['mac'], self.first_collector.mac)
        self.assertEqual(response_dict['collector_type'], self.first_collector.collector_type)

    def test_add_collector_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            method='post',
            resource='create',
            companies_pk=self.first_company.id
        )

    def test_add_collector_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            method='post',
            resource='create',
            companies_pk=self.first_company.id
        )
    
    def test_add_collector_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.index_route,
            self.unactivated_token,
            method='post',
            resource='create',
            companies_pk=self.first_company.id
        )

    def test_add_collector_response_is_201(self):
        collector_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'mac': '12232141',
            'collector_type': 'Wise',
        }

        request = factory.post(self.index_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = collector_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('UTF-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Collector.objects.filter(company=self.first_company).all()), 3)
        self.assertEqual(len(Collector.objects.all()), 4)
        self.assertEqual(response_dict['mac'], payload['mac'])
        self.assertEqual(response_dict['collector_type'], payload['collector_type'])

    def test_update_collector_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.single_route,
            method='put',
            resource='update',
            pk=self.first_company.id
        )
    
    def test_update_collector_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.single_route,
            method='put',
            resource='update',
            pk=self.first_company.id
        )

    def test_update_collector_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self, 
            self.single_route,
            self.unactivated_token,
            method='put',
            resource='update',
            pk=self.first_company.id
        )

    def test_update_collector_response_is_200(self):
        collector_view = views.CollectorViewSet.as_view({'put': 'update'})
        factory = APIRequestFactory()

        payload = {
            'mac': '12232144',
            'collector_type': 'HW',
        }

        request = factory.put(self.single_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = collector_view(request, companies_pk=self.first_company.id, pk=self.first_collector.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['mac'], payload['mac'])
        self.assertEqual(response_dict['collector_type'], payload['collector_type'])
    
    def test_destroy_collector_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.single_route,
            method='delete',
            resource='destroy',
            pk=self.first_collector.id
        )
    
    def test_destroy_collector_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.single_route,
            method='delete',
            resource='destroy',
            pk=self.first_collector.id
        )
    
    def test_destroy_collector_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.single_route,
            self.unactivated_token,
            method='delete',
            resource='destroy',
            pk=self.first_company.id
        )

    def test_destroy_collector_response_is_204(self):
        collector_view = views.CollectorViewSet.as_view({'delete': 'destroy'})
        factory = APIRequestFactory()

        request = factory.delete(self.single_route, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = collector_view(request, companies_pk=self.first_company.id, pk=self.first_collector.id)

        self.assertEqual(response.status_code, 204)