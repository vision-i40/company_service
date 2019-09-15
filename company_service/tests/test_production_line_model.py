from django.test import TestCase
from company_service.models import ProductionLine, Company, Product, ProductionOrder

class ProductionLineModelTest(TestCase):
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
        self.second_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="c2",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=10500)
        self.third_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="c3",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=11500)
        self.first_product = Product.objects.create(company=self.first_company, name="product one")
        self.first_released_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1001',
            quantity=100,
            state=ProductionOrder.RELEASED)
        self.second_released_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.third_production_line,
            code='1021',
            quantity=150,
            state=ProductionOrder.RELEASED)
        self.first_in_progress_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1002',
            quantity=1000,
            state=ProductionOrder.IN_PROGRESS)
        self.second_in_progress_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.second_production_line,
            code='1012',
            quantity=1200,
            state=ProductionOrder.IN_PROGRESS)


    def test_show_in_progress_production_order_in_the_line_retrieved(self):
        in_progress_order = self.first_production_line.in_progress_order()

        self.assertEqual(in_progress_order.id, self.first_in_progress_production_order.id)
        self.assertEqual(in_progress_order.state, self.first_in_progress_production_order.state)
        self.assertEqual(in_progress_order.code, self.first_in_progress_production_order.code)

    def test_show_no_progress_order_in_a_production_line_with_no_in_progress_order(self):
        none_order = self.third_production_line.in_progress_order()

        self.assertEqual(none_order, None)


