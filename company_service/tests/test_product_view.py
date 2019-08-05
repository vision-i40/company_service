from django.test import TestCase
from rest_framework.test import APIRequestFactory
from company_service import view as views
from users.models import User
from company_service.models import Company, Product
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.tests.view_test_support import *
import json


class ProductViewSetTest(TestCase):
    view = views.ProductViewSet

    def setUp(self):
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True)
        self.first_company = Company.objects.create(name="company one", slug="c1", is_active=True)
        self.first_product = Product.objects.create(company=self.first_company, name="product one",
                                                    production_rate_per_hour=10.1, description="A desc")
        self.second_product = Product.objects.create(company=self.first_company, name="product two",
                                                     production_rate_per_hour=10.2, description="Another desc")
        self.noise_company = Company.objects.create(name="company two", slug="c2", is_active=False)
        self.noise_product = Product.objects.create(company=self.noise_company, name="product noise",
                                                    production_rate_per_hour=10.3)
        self.active_user.companies.add(self.first_company)
        self.unactive_user = User.objects.create(email="unactivetest@test.com", password="any-pwd")
        self.unactive_user.companies.add(self.noise_company)
        active_refresh = RefreshToken.for_user(self.active_user)
        unactive_refresh = RefreshToken.for_user(self.unactive_user)
        self.active_token = str(active_refresh.access_token)
        self.unactive_token = str(unactive_refresh.access_token)

        self.index_route = '/v1/companies/{}/products'.format(self.first_company.id)
        self.single_route = '/v1/companies/{}/products/{}'.format(
            self.first_company.id,
            self.first_product.id)

    def tearDown(self):
        self.first_company.delete()
        self.noise_company.delete()
        self.active_user.delete()
        self.unactive_user.delete()

    def test_product_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_product_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_product_list_authentication_response_is_401_when_a_token_from_an_unactive_user_is_provided(self):
        assert_unauthorized_with_unactive_user(
            self,
            self.index_route,
            self.unactive_token,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_product_list_response_is_200(self):
        product_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = product_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['name'], self.second_product.name)
        self.assertEqual(response_dict['results'][0]['production_rate_per_hour'],
                         self.second_product.production_rate_per_hour)
        self.assertEqual(response_dict['results'][0]['description'], self.second_product.description)
        self.assertEqual(response_dict['results'][1]['name'], self.first_product.name)
        self.assertEqual(response_dict['results'][1]['production_rate_per_hour'],
                         self.first_product.production_rate_per_hour)
        self.assertEqual(response_dict['results'][1]['description'], self.first_product.description)

    def test_product_details_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.single_route,
            resource='retrieve',
            pk=self.first_product.id,
            companies_pk=self.first_company.id)

    def test_product_details_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.single_route,
            resource='retrieve',
            pk=self.first_product.id,
            companies_pk=self.first_company.id)

    def test_product_details_authentication_response_is_401_when_a_token_from_an_unactive_user_is_provided(self):
        assert_unauthorized_with_unactive_user(
            self,
            self.single_route,
            self.unactive_token,
            resource='retrieve',
            pk=self.first_product.id,
            companies_pk=self.first_company.id)

    def test_product_details_response_is_200(self):
        product_view = self.view.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = product_view(request, pk=self.first_product.id, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['name'], self.first_product.name)
        self.assertEqual(response_dict['production_rate_per_hour'], self.first_product.production_rate_per_hour)
        self.assertEqual(response_dict['description'], self.first_product.description)

    def test_product_details_response_is_404_when_product_is_from_another_company(self):
        product_view = self.view.as_view({'get': 'retrieve'})
        factory = APIRequestFactory()

        request = factory.get(self.single_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = product_view(request, pk=self.noise_product.id, companies_pk=self.noise_company.id)

        response.render()

        self.assertEqual(response.status_code, 404)

    def test_add_product_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(self, self.index_route, method='post',
                                          resource='create', companies_pk=self.first_company.id)

    def test_add_product_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(self, self.index_route, method='post',
                                               resource='create', companies_pk=self.first_company.id)

    def test_add_product_authentication_response_is_401_when_a_token_from_an_unactive_user_is_provided(self):
        assert_unauthorized_with_unactive_user(self, self.index_route, self.unactive_token, method='post',
                                               resource='create', companies_pk=self.first_company.id)

    def test_add_product_response_is_201(self):
        product_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'name': 'test product name',
            'description': 'a new desc',
            'production_rate_per_hour': 99.91,
        }

        request = factory.post(self.index_route, payload, format='json',
                               HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = product_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Product.objects.filter(company=self.first_company).all()), 3)
        self.assertEqual(len(Product.objects.all()), 4)
        self.assertEqual(response_dict['name'], payload['name'])
        self.assertEqual(response_dict['description'], payload['description'])
        self.assertEqual(response_dict['production_rate_per_hour'], payload['production_rate_per_hour'])
