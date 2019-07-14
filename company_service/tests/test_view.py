from django.test import TestCase
from rest_framework.test import APIRequestFactory
from company_service import view as views
from users.models import User
from company_service.models import Company
from rest_framework_simplejwt.tokens import RefreshToken
import json

class CompanyViewSetTest(TestCase):
    def setUp(self):
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True)
        self.first_company = Company.objects.create(name="company one", slug="c1", is_active=True)
        self.second_company = Company.objects.create(name="company two", slug="c2", is_active=False)
        self.noise_company = Company.objects.create(name="company two", slug="c2", is_active=False)
        self.active_user.companies.add(self.first_company, self.second_company)
        self.unactive_user = User.objects.create(email="unactivetest@test.com", password="any-pwd")
        self.unactive_user.companies.add(self.noise_company)
        active_refresh = RefreshToken.for_user(self.active_user)
        unactive_refresh = RefreshToken.for_user(self.unactive_user)
        self.active_token = str(active_refresh.access_token)
        self.unactive_token = str(unactive_refresh.access_token)
    
    def tearDown(self):
        self.active_user.delete()

    def test_authentication_response_is_401_when_there_is_no_authentication_token(self):
        company_view = views.CompanyViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies')
        response = company_view(request)

        self.assertEqual(response.status_code, 401)
        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))
        self.assertTrue("credentials were not provided" in response_dict['detail'])

    def test_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        company_view = views.CompanyViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies', HTTP_AUTHORIZATION='Bearer invalid.token')
        response = company_view(request)

        self.assertEqual(response.status_code, 401)
        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))
        self.assertTrue("Given token not valid" in response_dict['detail'])

    def test_authentication_response_is_401_when_a_token_from_an_unactive_user_is_provided(self):
        company_view = views.CompanyViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies', HTTP_AUTHORIZATION='Bearer {}'.format(self.unactive_token))
        response = company_view(request)

        self.assertEqual(response.status_code, 401)
        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))
        self.assertTrue("User is inactive" in response_dict['detail'])
    
    def test_authentication_response_is_200_when_a_valid_authentication_token_is_provided(self):
        company_view = views.CompanyViewSet.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get('/v1/companies', HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = company_view(request)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['name'], self.second_company.name)
        self.assertEqual(response_dict['results'][1]['name'], self.first_company.name)
        