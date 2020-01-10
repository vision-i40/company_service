# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from rest_framework_simplejwt.tokens import RefreshToken

# from company_service.models import ProductionEvent, Product, Company, StopCode, CodeGroup, ProductionChart, ProductionLine, ProductionOrder
# from company_service import view as views
# from users.models import User

# import json
# import datetime
# import pytz

# class ProductionChartTestCase(TestCase):
#     view = views.ProductionChartViewSet
#     test_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

#     def setUp(self):
#         self.first_company = Company.objects.create(trade_name="company one", slug="c1", is_active=True)
#         self.first_code_group = CodeGroup.objects.create(company=self.first_company, name="group-test", group_type="Stop Code")
#         self.first_stop_code = StopCode.objects.create(company=self.first_company, is_planned=False, name="stop code test", code_group=self.first_code_group)
#         self.first_product = Product.objects.create(company=self.first_company, name='product-test')
#         self.active_user = User.objects.create(email="test@test.com", password="any-pwd", is_active=True,
#                                                default_company=self.first_company)

#         self.first_production_line = ProductionLine.objects.create(
#             company=self.first_company,
#             name="c1",
#             is_active=True,
#             discount_rework=True,
#             discount_waste=True,
#             stop_on_production_absence=True,
#             time_to_consider_absence=True,
#             reset_production_changing_order=True,
#             micro_stop_seconds=10200)

#         self.first_production_order = ProductionOrder.objects.create(
#             product=self.first_product,
#             production_line=self.first_production_line,
#             code='1004',
#             quantity=1000,
#             state=ProductionOrder.IN_PROGRESS)

#         self.first_company.users.add(self.active_user)
#         active_refresh = RefreshToken.for_user(self.active_user)

#         self.active_token = str(active_refresh.access_token)
#         self.authorization_active_token = f'Bearer {self.active_token}'

#         self.index_route = f'/v1/companies/{self.first_company}/production_chart/'

#         production_events = [
#             self.create_production_event(ProductionEvent.PRODUCTION, 20, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 23, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
#             self.create_production_event(ProductionEvent.PRODUCTION, 12, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 28, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
#             self.create_production_event(ProductionEvent.PRODUCTION, 14, self.first_production_order, datetime.datetime(2019, 12, 26, 9, 33, 15, 940070, tzinfo=pytz.UTC).strftime(self.test_date_format)),
#         ]

#     def create_production_event(self, event_type, quantity, production_order, event_datetime):
#         return ProductionEvent.objects.create(
#             company=self.first_company,
#             production_line=self.first_production_line,
#             production_order=production_order,
#             product=self.first_product,
#             event_datetime=event_datetime,
#             quantity=quantity,
#             event_type=event_type)

#     def test_production_chart_list_response_is_200(self):
#         production_chart_view = self.view.as_view({'get': 'list'})
#         factory = APIRequestFactory()

#         request = factory.get(self.index_route, HTTP_AUTHORIZATION=self.authorization_active_token)
#         response = production_chart_view(request, companies_pk=self.first_company.id)

#         response.render()
#         response_dict = json.loads(response.content.decode('utf-8'))

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response_dict['results']), 1)

