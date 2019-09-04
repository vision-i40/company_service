from django.test import TestCase
from rest_framework.test import APIRequestFactory
from users.models import User
from company_service.models import Company
from users.view import UserViewSet
from company_service.tests.view_test_support import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSetTest(TestCase):
    view = UserViewSet

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)
        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd",
                                                    is_active=False)
        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)
        self.authorization_active_token = 'Bearer {}'.format(self.active_token)


    def test_current_user_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, route='/v1/users/current', method='get', resource='current')

    def test_current_user_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, route='/v1/users/current', method='get', resource='current')

    def test_current_user_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(self, route='/v1/users/current',
                                                  unactivatedToken=self.unactivated_token,
                                                  method='get', resource='current')

    def test_current_user_profile_info_response_is_200(self):
        user_view = UserViewSet.as_view({'get': 'current'})
        factory = APIRequestFactory()

        request = factory.get('/v1/users/current', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = user_view(request)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['id'], self.active_user.id)
        self.assertEqual(response_dict['name'], self.active_user.name)
        self.assertEqual(response_dict['email'], self.active_user.email)
        self.assertEqual(response_dict['is_active'], self.active_user.is_active)
        self.assertEqual(response_dict['default_company']['id'], self.first_company.id)
