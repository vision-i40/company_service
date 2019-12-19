from django.test import TestCase
from rest_framework.test import APIRequestFactory
from company_service import view as views
from users.models import User
from company_service.models import Company, Collector, Channel, ProductionLine
from rest_framework_simplejwt.tokens import RefreshToken
import json

class ChannelViewTestCase(TestCase):
    view = views.ChannelViewSet

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True, default_company=self.first_company)
        self.unactive_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd", is_active=False)

        self.first_collector = Collector.objects.create(company=self.first_company, mac="23123232", collector_type="Lora")
        self.second_collector = Collector.objects.create(company=self.first_company, mac="1223244", collector_type="HW")
        self.noise_collector = Collector.objects.create(company=self.noise_company, mac="", collector_type="collector-noise")

        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="pl1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=21200)

        self.first_channel = Channel.objects.create(collector=self.first_collector, production_line=self.first_production_line, number=1024, channel_type='Good', inverse_state=True, is_cumulative=True)
        self.second_channel = Channel.objects.create(collector=self.second_collector, production_line=self.first_production_line, number=2048, channel_type='Rework', inverse_state=False, is_cumulative=True)

        self.first_company.users.add(self.active_user)
        self.noise_company.users.add(self.unactive_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        unactive_refresh = RefreshToken.for_user(self.unactive_user)

        self.active_token = str(active_refresh.access_token)
        self.unactive_token = str(unactive_refresh.access_token)
        self.authorization_active_token = f'Bearer {self.active_token}'

        self.index_route = f'v1/companies/{self.first_company.id}/collectors/{self.first_collector.id}/channels'
        self.single_route = f'v1/companies/{self.first_company.id}/collectors/{self.first_collector.id}/channels/{self.first_channel.id}'

    def test_channel_list_response_is_200(self):
        channel_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
        response = channel_view(request, companies_pk=self.first_company.id, collectors_pk=self.first_collector.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 1)
        self.assertEqual(response_dict['results'][0]['number'], self.first_channel.number)

    def test_add_turn_response_is_201(self):
        channel_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'number': 3096,
            'channel_type': 'Good',
            'inverse_state': True,
            'is_cumulative': False
        }

        request = factory.post(self.index_route, payload, format='json', HTTP_AUTHORIZATION=self.authorization_active_token)
        response = channel_view(request, collectors_pk=self.first_collector.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_dict['number'], payload['number'])
        self.assertEqual(response_dict['channel_type'], payload['channel_type'])
        self.assertEqual(response_dict['inverse_state'], payload['inverse_state'])
        self.assertEqual(response_dict['is_cumulative'], payload['is_cumulative'])
