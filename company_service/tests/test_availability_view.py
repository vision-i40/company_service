from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.models import (Availability, Company, ProductionLine, 
                                    StateEvent, CodeGroup, StopCode)
from company_service import view as views
from company_service import choices
from company_service.tests.view_test_support import *
from users.models import User

import json
import datetime
import pytz

class AvailabilityViewSetTest(TestCase):
    view = views.AvailabilityViewSet
    test_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)
        self.first_code_group = CodeGroup.objects.create(company=self.first_company, name="group-test", group_type="Stop Code")
        self.first_stop_code = StopCode.objects.create(company=self.first_company, is_planned=False, name="stop code test", code_group=self.first_code_group)
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

        self.second_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="pl2",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=20500
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

        self.index_route = f'/v1/companies/{self.first_company.id}/availability/'

        self.state_events = [
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 12, 3, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.second_production_line, None, datetime.datetime(2019, 12, 3, 12, 3, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.second_production_line, None, datetime.datetime(2019, 12, 3, 12, 8, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 12, 50, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 13, 30, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.second_production_line, None, datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.second_production_line, None, datetime.datetime(2019, 12, 3, 12, 8, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON)
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

    def test_availability_list_response_is_200(self):
        availability_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 4)
        self.assertEqual(response_dict['results'][0]['start_datetime'], self.state_events[7].event_datetime)
        self.assertEqual(response_dict['results'][0]['end_datetime'], self.state_events[8].event_datetime)
        self.assertEqual(response_dict['results'][1]['start_datetime'], self.state_events[4].event_datetime)
        self.assertEqual(response_dict['results'][1]['end_datetime'], self.state_events[6].event_datetime)
        self.assertEqual(response_dict['results'][2]['start_datetime'], self.state_events[2].event_datetime)
        self.assertEqual(response_dict['results'][2]['end_datetime'], self.state_events[3].event_datetime)
        self.assertEqual(response_dict['results'][3]['start_datetime'], self.state_events[0].event_datetime)
        self.assertEqual(response_dict['results'][3]['end_datetime'], self.state_events[1].event_datetime)

    def test_the_availability_filtered_by_production_line(self):
        url = f'/v1/companies/1/availability/?production_line_id={self.first_production_line.id}&start_datetime=&end_datetime='

        availability_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(url, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)

    def test_the_availability_filtered_by_start_datetime(self):
        url = f'/v1/companies/1/availability/?production_line_id=&start_datetime={self.state_events[4].event_datetime}&end_datetime='

        availability_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(url, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)

    def test_the_availability_filtered_by_end_datetime(self):
        url = f'/v1/companies/1/availability/?production_line_id=&start_datetime=&end_datetime={self.state_events[1].event_datetime}'

        availability_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(url, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 1)