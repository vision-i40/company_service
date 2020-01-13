from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIRequestFactory

from company_service import view as views
from company_service.models import (Company, CodeGroup, StopCode, 
                                    StateEvent, ProductionLine, ManualStop)
from company_service import choices
from users.models import User

import json
import datetime
import pytz

class StateEventViewSetTest(TestCase):
    view = views.StateEventViewSet
    test_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.first_code_group = CodeGroup.objects.create(company=self.first_company, name="group-test", group_type="Stop Code")
        self.first_stop_code = StopCode.objects.create(company=self.first_company, is_planned=False, name="stop code test", code_group=self.first_code_group)
        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)

        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="pl1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=15800)

        self.state_events = [
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 10, 8, 8, 13, 45, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, self.first_stop_code, datetime.datetime(2019, 10, 8, 8, 18, 45, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.OFF),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 10, 8, 8, 13, 46, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON),
            self.create_state_event(self.first_production_line, None, datetime.datetime(2019, 10, 8, 8, 25, 46, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format), choices.ON)
        ]

        self.first_manual_stop = ManualStop.objects.create(
            production_line=self.first_production_line,
            start_datetime=datetime.datetime(2019, 10, 8, 8, 25, 47, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            end_datetime=datetime.datetime(2019, 10, 8, 9, 25, 47, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            stop_code=self.first_stop_code
        )

        self.first_company.users.add(self.active_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        self.active_token = str(active_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.index_route = f'/v1/companies/{self.first_company.id}/production_lines/{self.first_production_line.id}/state_events/'

    def tearDown(self):
        StateEvent.objects.all().delete()
        ManualStop.objects.all().delete()

    def create_state_event(self, production_line, stop_code, event_datetime, state):
        return StateEvent.objects.create(
            production_line=production_line,
            stop_code=stop_code,
            event_datetime=event_datetime,
            state=state
        )

    def test_state_event_list_response_is_200(self):
        state_event_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = state_event_view(request, companies_pk=self.first_company.id, production_lines_pk=self.first_production_line.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 6)
        self.assertEqual(response_dict['results'][0]['event_datetime'], self.first_manual_stop.end_datetime)
        self.assertEqual(response_dict['results'][1]['event_datetime'], self.first_manual_stop.start_datetime)
        self.assertEqual(response_dict['results'][2]['event_datetime'], self.state_events[3].event_datetime)
        self.assertEqual(response_dict['results'][3]['event_datetime'], self.state_events[2].event_datetime)
        self.assertEqual(response_dict['results'][4]['event_datetime'], self.state_events[1].event_datetime)
        self.assertEqual(response_dict['results'][5]['event_datetime'], self.state_events[0].event_datetime)

    def test_add_state_event_response_is_201(self):
        state_event_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'event_datetime': '2019-11-09T21:19:23Z',
            'stop_code_id': self.first_stop_code.id,
            'state': choices.OFF
        }

        request = factory.post(self.index_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = state_event_view(request, production_lines_pk=self.first_production_line.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_dict['event_datetime'], payload['event_datetime'])
        self.assertEqual(response_dict['stop_code_id'], payload['stop_code_id'])
        self.assertEqual(response_dict['state'], payload['state'])
