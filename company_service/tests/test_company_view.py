from django.test import TestCase
from rest_framework.test import APIRequestFactory
from company_service import view as views
from users.models import User
from company_service.models import Company
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import force_authenticate
from company_service.tests.view_test_support import *
import json


class CompanyViewSetTest(TestCase):
    view = views.CompanyViewSet

    def setUp(self):
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True)
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.second_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)
        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)
        self.first_company.users.add(self.active_user)
        self.second_company.users.add(self.active_user)
        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd", is_active=False)
        self.noise_company.users.add(self.unactivated_user)
        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)

        self.authorization_active_token = 'Bearer {}'.format(self.active_token)

    def tearDown(self):
        self.first_company.delete()
        self.second_company.delete()
        self.noise_company.delete()
        self.active_user.delete()
        self.unactivated_user.delete()

    def test_companies_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies', resource='list')

    def test_companies_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies', resource='list')

    def test_companies_list_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, 'v1/companies', self.unactivated_token, resource='list')

    def test_companies_list_response_is_200(self):
        company_view = views.CompanyViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['trade_name'], self.second_company.trade_name)
        self.assertEqual(response_dict['results'][1]['trade_name'], self.first_company.trade_name)

    def test_company_details_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies/{}'.format(self.first_company.id), resource='retrieve',
                                          pk=self.first_company.id)

    def test_company_details_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies/{}'.format(self.first_company.id),
                                               resource='retrieve', pk=self.first_company.id)

    def test_company_details_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, '/v1/companies/{}'.format(self.first_company.id),
                                               self.unactivated_token, resource='retrieve', pk=self.first_company.id)

    def test_company_details_response_is_200(self):
        company_view = views.CompanyViewSet.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies/{}'.format(self.first_company.id),
                              HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request, pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        response_dict['id'] = self.first_company.id
        response_dict['trade_name'] = self.first_company.trade_name

    def test_company_details_response_is_404_when_company_is_from_another_user(self):
        company_view = views.CompanyViewSet.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies/{}'.format(self.noise_company.id),
                              HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request, pk=self.noise_company.id)

        response.render()

        self.assertEqual(response.status_code, 404)

    def test_add_company_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies', method='post', resource='create')

    def test_add_company_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies', method='post', resource='create')

    def test_add_company_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, '/v1/companies', self.unactivated_token, method='post',
                                               resource='create')

    def test_add_company__response_is_201(self):
        company_view = views.CompanyViewSet.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'trade_name': 'test company trade_name',
            'slug': 'test-company-trade_name',
            'is_active': True,
        }

        request = factory.post('/v1/companies', payload, format='json',
                               HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Company.objects.get(pk=response_dict['id']).users.all()), 1)
        self.assertEqual(response_dict['trade_name'], payload['trade_name'])
        self.assertEqual(response_dict['slug'], payload['slug'])
        self.assertEqual(response_dict['is_active'], payload['is_active'])

    def test_update_company_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies/{}'.format(self.first_company.id), method='put',
                                          resource='update', pk=self.first_company.id)

    def test_update_company_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies/{}'.format(self.first_company.id), method='put',
                                               resource='update', pk=self.first_company.id)

    def test_update_company_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, '/v1/companies/{}'.format(self.first_company.id),
                                               self.unactivated_token, method='put', resource='update',
                                               pk=self.first_company.id)

    def test_update_company__response_is_200(self):
        company_view = views.CompanyViewSet.as_view({'put': 'update'})
        factory = APIRequestFactory()

        payload = {
            'trade_name': 'new test company trade_name',
            'slug': 'new-test-company-trade_name',
            'is_active': False,
        }

        request = factory.put('/v1/companies/{}'.format(self.first_company.id), payload, format='json',
                              HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request, pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.first_company.users.all()), 1)
        self.assertEqual(response_dict['trade_name'], payload['trade_name'])
        self.assertEqual(response_dict['slug'], payload['slug'])
        self.assertEqual(response_dict['is_active'], payload['is_active'])

    def test_destroy_company_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies/{}'.format(self.first_company.id), method='delete',
                                          resource='destroy', pk=self.first_company.id)

    def test_destroy_company_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies/{}'.format(self.first_company.id), method='delete',
                                               resource='destroy', pk=self.first_company.id)

    def test_destroy_company_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, '/v1/companies/{}'.format(self.first_company.id),
                                               self.unactivated_token, method='delete', resource='destroy',
                                               pk=self.first_company.id)

    def test_destroy_company__response_is_200(self):
        company_view = views.CompanyViewSet.as_view({'delete': 'destroy'})
        factory = APIRequestFactory()

        request = factory.delete('/v1/companies/{}'.format(self.first_company.id), format='json',
                                 HTTP_AUTHORIZATION=self.authorization_active_token)
        response = company_view(request, pk=self.first_company.id)

        self.assertEqual(response.status_code, 204)
