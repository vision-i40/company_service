from django.test import TestCase
from django.utils import timezone

from company_service.models import ProductionEvent, Product, Company, ReworkCode, WasteCode, CodeGroup, RejectChart, ProductionLine, ProductionOrder


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
            name="rework-group",
            group_type="Rework Code"
        )

        self.second_code_group = CodeGroup.objects.create(
            company=self.first_company,
            name="waste-group",
            group_type="Waste Code"
        )

        self.first_rework_code = ReworkCode.objects.create(
            company=self.first_company,
            name="rework code test",
            code_group=self.first_code_group,
        )

        self.first_waste_code = WasteCode.objects.create(
            company=self.first_company,
            name="waste code test",
            code_group=self.second_code_group,
        )

        self.first_product = Product.objects.create(
            company=self.first_company,
            name='product-test'
        )

        self.second_product = Product.objects.create(
            company=self.first_company,
            name='product-test2'
        )

        self.first_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1004',
            quantity=1000,
            state=ProductionOrder.IN_PROGRESS)

        self.first_reject_chart = RejectChart.objects.create(
            production_line=self.first_production_line,
            production_order=self.first_production_order
        )

        self.first_production_event = ProductionEvent.objects.create(
            company=self.first_company,
            production_line=self.first_production_line,
            production_order=self.first_production_order,
            product=self.first_product,
            event_datetime=timezone.now(),
            quantity=10,
            event_type=ProductionEvent.WASTE,
            waste_code=self.first_waste_code)

        self.second_production_event = ProductionEvent.objects.create(
            company=self.first_company,
            production_line=self.first_production_line,
            production_order=self.first_production_order,
            product=self.first_product,
            event_datetime=timezone.now(),
            quantity=6,
            event_type=ProductionEvent.REWORK,
            rework_code=self.first_rework_code)

    def test_reject_chart_instance(self):
        quantity_rejected = self.first_reject_chart.quantity_rejected()
        code_reason = self.first_reject_chart.code_reason()
        state = self.first_reject_chart.event_state()

        if state == ProductionEvent.WASTE:
            self.assertEqual(quantity_rejected, self.first_production_event.quantity)
            self.assertEqual(code_reason, self.first_production_event.waste_code)
            self.assertEqual(state, self.first_production_event.event_type)
        elif state == ProductionEvent.REWORK:
            self.assertEqual(quantity_rejected, self.second_production_event.quantity)
            self.assertEqual(code_reason, self.second_production_event.rework_code)
            self.assertEqual(state, self.second_production_event.event_type)

