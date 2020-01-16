from company_service.helpers.common_helpers import create_object_of, get_attribute_from_the_last_object_of

from charts.models import ProductionChart
from company_service.models import ProductionEvent

def create_production_chart_object():
    create_object_of(
        ProductionChart,
        production_line_id=get_attribute_from_the_last_object_of(ProductionEvent, 'production_line_id')['production_line_id'],
        production_order_id=get_attribute_from_the_last_object_of(ProductionEvent, 'production_order_id')['production_order_id'],
        start_datetime=get_attribute_from_the_last_object_of(ProductionEvent, 'event_datetime')['event_datetime'],
        end_datetime=get_attribute_from_the_last_object_of(ProductionEvent, 'event_datetime')['event_datetime'],
        quantity=get_attribute_from_the_last_object_of(ProductionEvent, 'quantity')['quantity'],
        product_id=get_attribute_from_the_last_object_of(ProductionEvent, 'product_id')['product_id'],
        event_type=get_attribute_from_the_last_object_of(ProductionEvent, 'event_type')['event_type']
    )

def update_production_chart_object():
    production_chart_object = ProductionChart.objects.filter(
        event_type=get_attribute_from_the_last_object_of(ProductionEvent, 'event_type')['event_type']
    ).order_by('created').last()
    production_chart_object.end_datetime = get_attribute_from_the_last_object_of(ProductionEvent, 'event_datetime')['event_datetime']
    production_chart_object.save()