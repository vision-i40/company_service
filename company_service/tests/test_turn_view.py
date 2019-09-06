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
                                              start_time="08:00", end_time="12:30", days_of_week=['2', '3', '4'])

        self.first_company.users.add(self.active_user)
        self.noise_company.users.add(self.unactivated_user)

        active_refresh = RefreshToken.for_user(self.active_user)
        unactivated_refresh = RefreshToken.for_user(self.unactivated_user)
        self.active_token = str(active_refresh.access_token)
        self.unactivated_token = str(unactivated_refresh.access_token)
        self.authorization_active_token = 'Bearer {}'.format(self.active_token)

        self.index_route = '/v1/companies/{}/turn_schemes/{}/turns/'.format(self.first_company.id, self.first_turn_scheme.id)
        self.single_route = '/v1/companies/{}/turn_schemes/{}/turns/{}'.format(self.first_company.id, self.first_turn_scheme.id, self.first_turn)

    def test_add_turn__response_is_201(self):
        turn_view = self.view.as_view({'post': 'create'})
        factory = APIRequestFactory()

        payload = {
            'name': 'turn-scheme-name',
            'start_time': '07:30',
            'end_time': '12:00',
            'days_of_week': ['1', '2', '3', '4', '5'],
        }

        request = factory.post(self.index_route, payload, format='json',
                               HTTP_AUTHORIZATION='Bearer {}'.format(self.active_token))
        response = turn_view(request, companies_pk=self.first_company.id, turn_schemes_pk=self.first_turn_scheme.id)

        response.render()
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        # self.assertEqual(len(TurnScheme.objects.filter(company=self.first_company).all()), 3)
        # self.assertEqual(len(TurnScheme.objects.all()), 4)
        # self.assertEqual(response_dict['name'], payload['name'])
