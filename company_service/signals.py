from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

from company_service.models import ManualStop, StateEvent, Availability, ProductionEvent
from company_service import models, choices

from charts.models import ProductionChart

def get_attribute_from_the_last_object_of(model, attribute):
    return model.objects.values(attribute).order_by('created').last()

def create_object_of(model, **kwargs):
    return model.objects.create(**kwargs)

@receiver(post_save, sender=ManualStop)
def post_save_manual_stop(sender, **kwargs):
    def create_state_events_using(manual_stop_datetime):
        create_object_of(
            StateEvent,
            production_line_id=get_attribute_from_the_last_object_of(ManualStop, 'production_line_id')['production_line_id'],
            stop_code_id=get_attribute_from_the_last_object_of(ManualStop, 'stop_code_id')['stop_code_id'],
            event_datetime=manual_stop_datetime,
            state=choices.OFF
        )

    manual_stop_start_datetime = get_attribute_from_the_last_object_of(ManualStop, 'start_datetime')['start_datetime']
    manual_stop_end_datetime = get_attribute_from_the_last_object_of(ManualStop, 'end_datetime')['end_datetime']

    create_state_events_using(manual_stop_start_datetime)
    create_state_events_using(manual_stop_end_datetime)

def compare_attributes_of_the_last_object(first_model, first_attribute, second_model, second_attribute):
    return get_attribute_from_the_last_object_of(first_model, first_attribute) == get_attribute_from_the_last_object_of(second_model, second_attribute)

@receiver(post_save, sender=StateEvent)
def post_save_state_event(sender, **kwargs):
    def create_availability_object():
        create_object_of(
            Availability, 
            production_line_id=get_attribute_from_the_last_object_of(StateEvent, 'production_line_id')['production_line_id'],
            start_datetime=get_attribute_from_the_last_object_of(StateEvent, 'event_datetime')['event_datetime'],
            end_datetime=get_attribute_from_the_last_object_of(StateEvent, 'event_datetime')['event_datetime'],
            state=get_attribute_from_the_last_object_of(StateEvent, 'state')['state'],
            stop_code_id=get_attribute_from_the_last_object_of(StateEvent, 'stop_code_id')['stop_code_id'],
        )

    def update_availability_object():
        availability_object = Availability.objects.filter(
            Q(state=get_attribute_from_the_last_object_of(StateEvent, 'state')['state']) &
            Q(stop_code=get_attribute_from_the_last_object_of(StateEvent, 'stop_code_id')['stop_code_id'])
        ).order_by('created').last()
        availability_object.end_datetime = get_attribute_from_the_last_object_of(StateEvent, 'event_datetime')['event_datetime']
        availability_object.save()

    state_events_production_line_equals_availabilitys_production_line = compare_attributes_of_the_last_object(StateEvent, 'production_line_id', Availability, 'production_line_id')
    state_events_state_equals_availabilitys_state = compare_attributes_of_the_last_object(StateEvent, 'state', Availability, 'state')
    state_events_stop_code_equals_availabilitys_stop_code = compare_attributes_of_the_last_object(StateEvent, 'state', Availability, 'state')

    if (state_events_state_equals_availabilitys_state and 
        state_events_stop_code_equals_availabilitys_stop_code and 
        state_events_production_line_equals_availabilitys_production_line):
        update_availability_object()
    else:
        create_availability_object()

@receiver(post_save, sender=ProductionEvent)
def post_save_production_event(sender, **kwargs):
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

    production_event_production_line_equals_production_chart_production_line = compare_attributes_of_the_last_object(ProductionEvent, 'production_line_id', ProductionChart, 'production_line_id')
    production_event_type_equals_production_chart_type = compare_attributes_of_the_last_object(ProductionEvent, 'event_type', ProductionChart, 'event_type')

    if (production_event_production_line_equals_production_chart_production_line and 
        production_event_type_equals_production_chart_type):
        update_production_chart_object()
    else:
        create_production_chart_object()
