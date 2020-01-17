from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.models import (Company, ProductionLine, 
                                    StateEvent, CodeGroup, StopCode)
from charts import views
from company_service import choices
from company_service.tests.view_test_support import *
from users.models import User

import json
import datetime
import pytz

class AvailabilityChartViewSetTest(TestCase):
    view = views.AvailabilityChartViewSet
    test_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)
        self.first_code_group = CodeGroup.objects.create(company=self.first_company, name="group-test", group_type="Stop Code")
        self.first_stop_code = StopCode.objects.create(company=self.first_company, is_planned=False, name="stop code test", code_group=self.first_code_group)
        self.second_stop_code = StopCode.objects.create(company=self.first_company, is_planned=True, name="stop code test 2", code_group=self.first_code_group)
        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="c1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=10200
        )

        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.first_company.users.add(self.active_user)
        active_refresh = RefreshToken.for_user(self.active_user)

        self.active_token = str(active_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd", is_active=False)
        self.noise_company.users.add(self.unactivated_user)

        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.unactivated_token = str(unactivated_refresh.access_token)

        self.index_route = f'/v1/companies/{self.first_company.id}/charts/availability_chart/'

        self.state_events = [
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2020, 1, 3, 10, 33, 15, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2020, 1, 3, 11, 38, 15, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2020, 1, 3, 11, 38, 16, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2020, 1, 3, 12, 0, 1, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, self.second_stop_code, datetime.datetime(2020, 1, 3, 12, 0, 1, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, self.second_stop_code, datetime.datetime(2020, 1, 3, 12, 34, 15, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
        ]
    
    def create_state_event(self, production_line, stop_code, event_datetime, state):
        return StateEvent.objects.create(
            production_line=production_line,
            stop_code=stop_code,
            event_datetime=event_datetime,
            state=state
        )

    def tearDown(self):
        StateEvent.objects.all().delete()

    def test_availability_list_authentication_response_is_401_when_there_is_no_authentication_token(self):
        assert_unauthorized_with_no_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_availability_list_authentication_response_is_401_when_an_invalid_authentication_token_is_provided(self):
        assert_unauthorized_with_invalid_token(
            self,
            self.index_route,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_availability_list_authentication_response_is_401_when_a_token_from_an_unactivated_user_is_provided(self):
        assert_unauthorized_with_unactivated_user(
            self,
            self.index_route,
            self.unactivated_token,
            resource='list',
            companies_pk=self.first_company.id
        )

    def test_availability_chart_list_response_is_200(self):
        availability_chart_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_chart_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['start_datetime'], self.state_events[4].event_datetime)
        self.assertEqual(response_dict['results'][0]['end_datetime'], self.state_events[5].event_datetime)
        self.assertEqual(response_dict['results'][1]['start_datetime'], self.state_events[0].event_datetime)
        self.assertEqual(response_dict['results'][1]['end_datetime'], self.state_events[1].event_datetime)