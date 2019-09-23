from django.test import TestCase
from company_service.models import ProductionLine, Company, Product, ProductionOrder, ProductionEvent
from django.utils import timezone

class ProductionOrderModelTest(TestCase):
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
        self.first_product = Product.objects.create(company=self.first_company, name="product one")
        self.first_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1002',
            quantity=1000,
            state=ProductionOrder.IN_PROGRESS)
        self.second_production_order = ProductionOrder.objects.create(
            product=self.first_product,
            production_line=self.first_production_line,
            code='1012',
            quantity=1200,
            state=ProductionOrder.IN_PROGRESS)
        self.create_production_event(ProductionEvent.PRODUCTION, 15, self.first_production_order)
        self.create_production_event(ProductionEvent.PRODUCTION, 5, self.first_production_order)
        self.create_production_event(ProductionEvent.PRODUCTION, 10, self.first_production_order)
        self.create_production_event(ProductionEvent.WASTE, 1, self.second_production_order)
        self.create_production_event(ProductionEvent.WASTE, 2, self.second_production_order)
        self.create_production_event(ProductionEvent.WASTE, 3, self.first_production_order)
        self.create_production_event(ProductionEvent.REWORK, 5, self.second_production_order)
        self.create_production_event(ProductionEvent.REWORK, 6, self.first_production_order)
        self.create_production_event(ProductionEvent.REWORK, 4, self.first_production_order)

    def create_production_event(self, event_type, quantity, production_order):
        return ProductionEvent.objects.create(
            company=self.first_company,
            production_line=self.first_production_line,
            production_order=production_order,
            product=self.first_product,
            event_datetime=timezone.now(),
            quantity=quantity,
            event_type=event_type)


    def test_show_in_production_quantity_in_the_production_order_retrieved(self):
        production_quantity = self.first_production_order.production_quantity()

        self.assertEqual(production_quantity, 30)

    def test_show_in_waste_quantity_in_the_production_order_retrieved(self):
        waste_quantity = self.second_production_order.waste_quantity()

        self.assertEqual(waste_quantity, 3)

    def test_show_in__quantity_in_the_production_order_retrieved(self):
        rework_quantity = self.first_production_order.rework_quantity()

        self.assertEqual(rework_quantity, 10)


