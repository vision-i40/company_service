from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

from company_service.models import ManualStop, StateEvent, Availability, ProductionEvent, ProductionChart
from company_service import models, choices

def get_attribute_of_the_last_object_from(model, attribute):
    return model.objects.values(attribute).order_by('created').last()[attribute]

@receiver(post_save, sender=ManualStop)
def post_save_manual_stop(sender, **kwargs):
    def create_state_events_using(manual_stop_datetime):
        StateEvent.objects.create(
            production_line_id=get_attribute_of_the_last_object_from(ManualStop, 'production_line_id'),
            stop_code_id=get_attribute_of_the_last_object_from(ManualStop, 'stop_code_id'),
            event_datetime=manual_stop_datetime,
            state=choices.OFF
        )

    manual_stop_start_datetime = get_attribute_of_the_last_object_from(ManualStop, 'start_datetime')
    manual_stop_end_datetime = get_attribute_of_the_last_object_from(ManualStop, 'end_datetime')

    create_state_events_using(manual_stop_start_datetime)
    create_state_events_using(manual_stop_end_datetime)

@receiver(post_save, sender=StateEvent)
def post_save_state_event(sender, **kwargs):
    def create_availability_object():
        Availability.objects.create(
            production_line_id=get_attribute_of_the_last_object_from(StateEvent, 'production_line_id'),
            start_datetime=get_attribute_of_the_last_object_from(StateEvent, 'event_datetime'),
            end_datetime=get_attribute_of_the_last_object_from(StateEvent, 'event_datetime'),
            state=get_attribute_of_the_last_object_from(StateEvent, 'state'),
            stop_code_id=get_attribute_of_the_last_object_from(StateEvent, 'stop_code_id')
        )

    def update_availability_object():
        availability_object = Availability.objects.filter(
            Q(state=get_attribute_of_the_last_object_from(StateEvent, 'state')) &
            Q(stop_code=get_attribute_of_the_last_object_from(StateEvent, 'stop_code_id'))
        ).order_by('created').last()
        availability_object.end_datetime = get_attribute_of_the_last_object_from(StateEvent, 'event_datetime')
        availability_object.save()

    if StateEvent.objects.values('state').order_by('created').last() == Availability.objects.values('state').order_by('created').last() and StateEvent.objects.values('stop_code_id').order_by('created').last() == Availability.objects.values('stop_code_id').order_by('created').last():
        update_availability_object()
    else:
        create_availability_object()
