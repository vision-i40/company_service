from django.dispatch import receiver
from django.db.models.signals import post_save

from company_service.models import ProductionEvent
from .models import ProductionChart

from company_service.helpers import common_helpers
from .helpers import production_event_helpers

@receiver(post_save, sender=ProductionEvent)
def post_save_production_event(sender, **kwargs):
    production_event_production_line_equals_production_chart_production_line = common_helpers.compare_attributes_of_the_last_object(ProductionEvent, 'production_line_id', ProductionChart, 'production_line_id')
    production_event_type_equals_production_chart_type = common_helpers.compare_attributes_of_the_last_object(ProductionEvent, 'event_type', ProductionChart, 'event_type')

    if (production_event_production_line_equals_production_chart_production_line and 
        production_event_type_equals_production_chart_type):
        production_event_helpers.update_production_chart_object()
    else:
        production_event_helpers.create_production_chart_object()