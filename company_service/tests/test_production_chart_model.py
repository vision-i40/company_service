from django.test import TestCase
from company_service.models import ProductionEvent, Product, Company, StopCode, CodeGroup, ProductionChart, ProductionLine, ProductionOrder, StateEvent

import datetime
import pytz

class ProductionChartTestCase(TestCase):
    def setUp(self):
        self.first_company = Company.objects.create(
                trade_name="company one",
                slug="c1",
                is_active=True)

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

        self.first_code_group = CodeGroup.objects.create(
            company=self.first_company,
            name="group-test",
            group_type="Stop Code"
        )

        self.first_stop_code = StopCode.objects.create(
            company=self.first_company,
            is_planned=False,
            name="stop code test",
            code_group=self.first_code_group,
        )

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

        self.first_production_chart = ProductionChart.objects.create(
            production_line=self.first_production_line,
            production_order=self.first_production_order
        )

        self.first_production_event = ProductionEvent.objects.create(
            company=self.first_company,
            product=self.first_product,
            production_line=self.first_production_line,
            production_order=self.first_production_order,
            quantity=500,
            event_type=ProductionEvent.PRODUCTION,
            event_datetime=datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC),
            production_chart=self.first_production_chart
        )

        self.first_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

    def test_production_chart_instance(self):
        start_datetime = self.first_production_chart.production_start()
        end_datetime = self.first_production_chart.production_end()
        quantity_produced = self.first_production_chart.quantity_produced()
        product = self.first_production_chart.product_produced()

        self.assertEqual(self.first_production_event.event_datetime, start_datetime)
        self.assertEqual(self.first_state_event.event_datetime, end_datetime)
        self.assertEqual(self.first_production_event.quantity, quantity_produced)
        self.assertEqual(self.first_production_event.product.id, product.id)
