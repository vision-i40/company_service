from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from company_service import view as views
from company_service.models import Company, TurnScheme, Turn
from company_service.tests.view_test_support import *
from users.models import User


class TurnSetTest(TestCase):
    view = views.TurnViewSet

    def setUp(self):
        self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
        self.noise_company = Company.objects.create(trade_name="company two", slug="c2", is_active=False)

        self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
                                               default_company=self.first_company)
        self.unactivated_user = User.objects.create(email="unactivatedtest@test.com", password="any-pwd",
                                                    is_active=False)

        self.first_turn_scheme = TurnScheme.objects.create(company=self.first_company, name="turn_scheme one")
        self.second_turn_scheme = TurnScheme.objects.create(company=self.first_company, name="turn_scheme two")
        self.noise_turn_scheme = TurnScheme.objects.create(company=self.noise_company, name="turn_scheme noise")

        self.first_turn = Turn.objects.create(turn_scheme=self.first_turn_scheme, name="turn 1",
                                              start_time="08:00:12", end_time="12:30:23", days_of_week=[4, 5, 6])
        self.second_turn = Turn.objects.create(turn_scheme=self.first_turn_scheme, name="turn 2",
                                              start_time="08:00:23", end_time="12:40:21", days_of_week=[1, 2, 3])
        self.third_turn = Turn.objects.create(turn_scheme=self.second_turn_scheme, name="turn 3",
                                              start_time="08:00:23", end_time="12:40:21", days_of_week=[1, 2, 3])

        self.first_company.users.add(self.active_user)
        self.noise_company.users.add(self.unactivated_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)
        self.authorization_active_token = 'Bearer {}'.format(self.active_token)

        self.index_route = '/v1/companies/{}/turn_schemes/{}/turns/'.format(self.first_company.id, self.first_turn_scheme.id)
        self.single_route = '/v1/companies/{}/turn_schemes/{}/turns/{}'.format(self.first_company.id, self.first_turn_scheme.id, self.first_turn)

    def test_turn_list_response_is_200(self):
        turn_view = self.view.as_view({'get': 'list'})
        factory = APIRequestFactory()

        request = factory.get(self.index_route, HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_view(request, companies_pk=self.first_company.id, turn_schemes_pk=self.first_turn_scheme.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_dict['results']), 2)
        self.assertEqual(response_dict['results'][0]['name'], self.second_turn.name)
        self.assertEqual(response_dict['results'][1]['name'], self.first_turn.name)

    def test_add_turn__response_is_201(self):
        turn_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'name': 'turn-scheme-name',
            'start_time': '07:30:15',
            'end_time': '12:00:25',
            'days_of_week': [1, 2, 3, 4],
        }

        request = factory.post(self.index_route, payload, format='json',
                               HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_view(request, turn_schemes_pk=self.first_turn_scheme.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_dict['name'], payload['name'])
        self.assertEqual(response_dict['start_time'], payload['start_time'])
        self.assertEqual(response_dict['end_time'], payload['end_time'])
        self.assertEqual(response_dict['days_of_week'], payload['days_of_week'])
