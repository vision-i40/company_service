from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

from company_service.models import ManualStop, StateEvent, Availability, ProductionEvent
from company_service import models, choices
from company_service.helpers import common_helpers, manual_stop_helpers, state_event_helpers, production_event_helpers
from charts.models import ProductionChart

@receiver(post_save, sender=ManualStop)
def post_save_manual_stop(sender, **kwargs):
    manual_stop_start_datetime = common_helpers.get_attribute_from_the_last_object_of(ManualStop, 'start_datetime')['start_datetime']
    manual_stop_end_datetime = common_helpers.get_attribute_from_the_last_object_of(ManualStop, 'end_datetime')['end_datetime']

    manual_stop_helpers.create_state_events_using(manual_stop_start_datetime)
    manual_stop_helpers.create_state_events_using(manual_stop_end_datetime)

@receiver(post_save, sender=StateEvent)
def post_save_state_event(sender, **kwargs):
    state_events_production_line_equals_availabilitys_production_line = common_helpers.compare_attributes_of_the_last_object(StateEvent, 'production_line_id', Availability, 'production_line_id')
    state_events_state_equals_availabilitys_state = common_helpers.compare_attributes_of_the_last_object(StateEvent, 'state', Availability, 'state')
    state_events_stop_code_equals_availabilitys_stop_code = common_helpers.compare_attributes_of_the_last_object(StateEvent, 'state', Availability, 'state')

    if (state_events_state_equals_availabilitys_state and 
        state_events_stop_code_equals_availabilitys_stop_code and 
        state_events_production_line_equals_availabilitys_production_line):
        state_event_helpers.update_availability_object()
    else:
        state_event_helpers.create_availability_object()

@receiver(post_save, sender=ProductionEvent)
def post_save_production_event(sender, **kwargs):
    production_event_production_line_equals_production_chart_production_line = common_helpers.compare_attributes_of_the_last_object(ProductionEvent, 'production_line_id', ProductionChart, 'production_line_id')
    production_event_type_equals_production_chart_type = common_helpers.compare_attributes_of_the_last_object(ProductionEvent, 'event_type', ProductionChart, 'event_type')

    if (production_event_production_line_equals_production_chart_production_line and 
        production_event_type_equals_production_chart_type):
        production_event_helpers.update_production_chart_object()
    else:
        production_event_helpers.create_production_chart_object()
