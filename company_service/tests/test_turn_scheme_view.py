from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from company_service import view as views
from company_service.models import Company, TurnScheme
from company_service.tests.view_test_support import *
from users.models import User


class TurnSchemeSetTest(TestCase):
    view = views.TurnSchemeViewSet

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)
        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd",
                                                    is_active=False)

        self.first_turn_scheme = TurnScheme.objects.create(company=self.first_company, name="turn_scheme one")
        self.second_turn_scheme = TurnScheme.objects.create(company=self.first_company, name="turn_scheme two")
        self.noise_turn_scheme = TurnScheme.objects.create(company=self.noise_company, name="turn_scheme noise")

        self.first_company.users.add(self.active_user)
        self.noise_company.users.add(self.unactivated_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)
        self.authorization_active_token = 'Bearer {}'.format(self.active_token)

        self.index_route = '/v1/companies/{}/turn_schemes'.format(self.first_company.id)
        self.single_route = '/v1/companies/{}/turn_schemes/{}'.format(self.first_company.id, self.first_turn_scheme.id)

    def test_turn_scheme_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_turn_scheme_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_turn_scheme_list_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.index_route,
            self.unactivated_token,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_turn_scheme_list_response_is_200(self):
        turn_scheme_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_scheme_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['name'], self.second_turn_scheme.name)
        self.assertEqual(response_dict['results'][1]['name'], self.first_turn_scheme.name)

    def test_turn_scheme_details_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.single_route,
            resource='retrieve',
            pk=self.first_turn_scheme.id,
            companies_pk=self.first_company.id)

    def test_turn_scheme_details_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.single_route,
            resource='retrieve',
            pk=self.first_turn_scheme.id,
            companies_pk=self.first_company.id)

    def test_turn_scheme_details_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.single_route,
            self.unactivated_token,
            resource='retrieve',
            pk=self.first_turn_scheme.id,
            companies_pk=self.first_company.id)

    def test_turn_scheme_details_response_is_404_when_turn_scheme_is_from_another_company(self):
        turn_scheme_view = self.view.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_scheme_view(request, pk=self.noise_turn_scheme.id, companies_pk=self.noise_company.id)

        response.render()

        self.assertEqual(response.status_code, 404)

    def test_turn_scheme_details_response_is_200(self):
        turn_scheme_view = self.view.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_scheme_view(request, pk=self.first_turn_scheme.id, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['name'], self.first_turn_scheme.name)

    def test_add_turn_scheme_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, self.index_route, method='post',
                                          resource='create', companies_pk=self.first_company.id)

    def test_add_turn_scheme_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, self.index_route, method='post',
                                               resource='create', companies_pk=self.first_company.id)

    def test_add_turn_scheme_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, self.index_route, self.unactivated_token, method='post',
                                                  resource='create', companies_pk=self.first_company.id)

    def test_add_turn_scheme__response_is_201(self):
        turn_scheme_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'name': 'turn-scheme-name',
        }

        request = factory.post(self.index_route, payload, format='json',
                               HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_scheme_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(TurnScheme.objects.filter(company=self.first_company).all()), 3)
        self.assertEqual(len(TurnScheme.objects.all()), 4)
        self.assertEqual(response_dict['name'], payload['name'])

    def test_update_turn_scheme_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, '/v1/companies/{}/turn_schemes/{}'.
                                          format(self.first_company.id, self.first_turn_scheme.id),
                                          method='put', resource='update', pk=self.first_company.id)

    def test_update_turn_scheme_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, '/v1/companies/{}/turn_schemes/{}'.
                                               format(self.first_company.id, self.first_turn_scheme.id),
                                               method='put', resource='update', pk=self.first_company.id)

    def test_update_turn_scheme_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, '/v1/companies/{}/turn_schemes/{}'.
                                                  format(self.first_company.id, self.first_turn_scheme.id),
                                                  self.unactivated_token, method='put', resource='update',
                                                  pk=self.first_company.id)
