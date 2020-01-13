from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIRequestFactory

from company_service import view as views
from company_service.models import ManualStop, ProductionLine, StopCode, CodeGroup, Company
from company_service.serializers import ManualStopSerializer
from users.models import User

import json
import datetime
import pytz

class ManualStopViewSetTest(TestCase):
    view = views.ManualStopViewSet
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

        self.first_manual_stop = ManualStop.objects.create(
            production_line=self.first_production_line,
            start_datetime=datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            end_datetime=datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            stop_code=self.first_stop_code
        )

        self.second_manual_stop = ManualStop.objects.create(
            production_line=self.first_production_line,
            start_datetime=datetime.datetime(2019, 12, 3, 21, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            end_datetime=datetime.datetime(2019, 12, 3, 22, 3, 55, 988870, tzinfo=pytz.UTC).strftime(self.test_date_format),
            stop_code=self.first_stop_code
        )

        self.first_company.users.add(self.active_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        self.active_token = str(active_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.index_route = f'/v1/companies/{self.first_company.id}/production_lines/{self.first_production_line.id}/manual_stops/'

    def tearDown(self):
        ManualStop.objects.all().delete()

    def test_manual_stop_list_response_is_200(self):
        manual_stop_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = manual_stop_view(request, companies_pk=self.first_company.id, production_lines_pk=self.first_production_line.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['start_datetime'], self.second_manual_stop.start_datetime)
        self.assertEqual(response_dict['results'][0]['end_datetime'], self.second_manual_stop.end_datetime)
        self.assertEqual(response_dict['results'][1]['start_datetime'], self.first_manual_stop.start_datetime)
        self.assertEqual(response_dict['results'][1]['end_datetime'], self.first_manual_stop.end_datetime)

    def test_add_manual_stop_response_is_201(self):
        manual_stop_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'start_datetime': '2019-10-14T11:39:13Z',
            'end_datetime': '2019-10-14T12:39:13Z',
            'stop_code_id': self.first_stop_code.id
        }

        request = factory.post(self.index_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = manual_stop_view(request, production_lines_pk=self.first_production_line.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_dict['start_datetime'], payload['start_datetime'])
        self.assertEqual(response_dict['end_datetime'], payload['end_datetime'])
        self.assertEqual(response_dict['stop_code_id'], payload['stop_code_id'])

    def test_add_manual_stop_with_start_datetime_higher_than_end_datetime_response_is_400(self):
        manual_stop_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'start_datetime': '2019-10-14T18:39:13Z',
            'end_datetime': '2019-10-13T16:14:03Z',
            'stop_code_id': self.first_stop_code.id
        }

        request = factory.post(self.index_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = manual_stop_view(request, production_lines_pk=self.first_production_line.id)

        response.render()

        self.assertEqual(response.status_code, 400)

