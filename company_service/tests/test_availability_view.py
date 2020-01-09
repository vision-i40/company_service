from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from company_service.models import Availability, Company, ProductionLine, StateEvent, CodeGroup, StopCode
from company_service import view as views
from company_service.tests.view_test_support import *
from company_service import choices
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

        self.first_company.users.add(self.active_user)
        active_refresh = RefreshToken.for_user(self.active_user)

        self.active_token = str(active_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.index_route = f'/v1/companies/{self.first_company.id}/availability/'

        self.state_event_list = [
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 12, 3, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            # self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            # self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 12, 50, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            # self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 12, 3, 13, 30, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            # self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 13, 40, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            # self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 12, 3, 13, 45, 54, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON)
        ]

    def create_state_event(self, production_line, stop_code, event_datetime, state):
        return StateEvent.objects.create(
            production_line=production_line,
            stop_code=stop_code,
            event_datetime=event_datetime,
            state=state
        )

    def test_availability_list_response_is_200(self):
        availability_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = availability_view(request, companies_pk=self.first_company.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 1)
        self.assertEqual(response_dict['results'][0]['start_datetime'], self.state_event_list[0].event_datetime)
        self.assertEqual(response_dict['results'][0]['end_datetime'], self.state_event_list[1].event_datetime)
        # self.assertEqual(response_dict['results'][1]['start_datetime'], self.state_event_list[2].event_datetime)
