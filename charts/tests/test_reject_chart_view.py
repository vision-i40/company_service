from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.models import (ProductionEvent, Product, Company, 
                                    CodeGroup, ProductionLine, ProductionOrder)
from charts import views
from users.models import User
from company_service.tests.view_test_support import *

import json
import datetime
import pytz

class ProductionChartTestCase(TestCase):
    view = views.RejectChartViewSet
    test_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    def setUp(self):
        self.first_company = Company.objects.create(
                trade_name="company one",
                slug="c1",
                is_active=True)
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)

        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="c1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=10200)

        self.first_product = Product.objects.create(
            company=self.first_company,
            name='product-test'
        )

        self.first_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1004',
            quantity=1000,
            state=ProductionOrder.IN_PROGRESS)

        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.first_company.users.add(self.active_user)
        active_refresh = RefreshToken.for_user(self.active_user)

        self.active_token = str(active_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd", is_active=False)
        self.noise_company.users.add(self.unactivated_user)

        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.unactivated_token = str(unactivated_refresh.access_token)

        self.index_route = f'/v1/companies/{self.first_company.id}/charts/reject_chart/'

        self.production_events = [
            self.create_production_event(ProductionEvent.PRODUCTION, 47, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 23, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.PRODUCTION, 32, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 28, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.WASTE, 14, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 33, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.WASTE, 5, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 38, 25, 840070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.WASTE, 8, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 48, 15, 840070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.REWORK, 7, self.first_production_order, datetime.datetime(2019, 12, 26, 10, 15, 5, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
            self.create_production_event(ProductionEvent.REWORK, 12, self.first_production_order, datetime.datetime(2019, 12, 26, 10, 59, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
        ]

    def create_production_event(self, event_type, quantity, production_order, event_datetime):
        return ProductionEvent.objects.create(
            company=self.first_company,
            production_line=self.first_production_line,
            production_order=production_order,
            product=self.first_product,
            event_datetime=event_datetime,
            quantity=quantity,
            event_type=event_type)

    def tearDown(self):
        ProductionEvent.objects.all().delete()

    def test_reject_chart_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_reject_chart_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_reject_chart_list_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.index_route,
            self.unactivated_token,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_reject_chart_list_response_is_200(self):
        reject_chart_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = reject_chart_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['start_datetime'], self.production_events[5].event_datetime)
        self.assertEqual(response_dict['results'][0]['end_datetime'], self.production_events[6].event_datetime)
        self.assertEqual(response_dict['results'][0]['quantity'], 19)
        self.assertEqual(response_dict['results'][1]['start_datetime'], self.production_events[2].event_datetime)
        self.assertEqual(response_dict['results'][1]['end_datetime'], self.production_events[4].event_datetime)
        self.assertEqual(response_dict['results'][1]['quantity'], 27)