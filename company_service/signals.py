from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

from company_service.models import ManualStop, StateEvent, Availability, ProductionEvent, ProductionChart
from company_service import models, choices

def get_attribute_of_the_first_object_from(attribute, *args, model=StateEvent):
    return model.objects.values(attribute).order_by(*args).first()[attribute]

@receiver(post_save, sender=ManualStop)
def post_save_manual_stop(sender, **kwargs):
    def create_state_events_using(manual_stop_datetime):
        StateEvent.objects.create(
            production_line_id=get_attribute_of_the_first_object_from('production_line_id', '-start_datetime', model=ManualStop),
            stop_code_id=get_attribute_of_the_first_object_from('stop_code_id', '-start_datetime', model=ManualStop),
            event_datetime=manual_stop_datetime,
            state=choices.OFF
        )

    manual_stop_start_datetime = get_attribute_of_the_first_object_from('start_datetime', '-start_datetime', model=ManualStop)
    manual_stop_end_datetime = get_attribute_of_the_first_object_from('end_datetime', '-start_datetime', model=ManualStop)

    create_state_events_using(manual_stop_start_datetime)
    create_state_events_using(manual_stop_end_datetime)

@receiver(post_save, sender=StateEvent)
def post_save_state_event(sender, **kwargs):
    def create_availability_object():
        Availability.objects.create(
            production_line_id=get_attribute_of_the_first_object_from('production_line_id', '-event_datetime'),
            start_datetime=get_attribute_of_the_first_object_from('event_datetime', 'event_datetime'),
            end_datetime=get_attribute_of_the_first_object_from('event_datetime', '-event_datetime'),
            state=get_attribute_of_the_first_object_from('state', '-event_datetime'),
            stop_code_id=get_attribute_of_the_first_object_from('stop_code_id', '-event_datetime')
        )

    def update_availability_object():
        availability_object = Availability.objects.filter(
            Q(state=get_attribute_of_the_first_object_from('state', '-event_datetime')) &
            Q(stop_code=get_attribute_of_the_first_object_from('stop_code_id', '-event_datetime'))
        ).order_by('-start_datetime', '-end_datetime').first()
        availability_object.end_datetime = get_attribute_of_the_first_object_from('event_datetime', '-event_datetime')
        availability_object.save()

    if StateEvent.objects.values('state').order_by('-event_datetime').first() == Availability.objects.values('state').order_by('-end_datetime').first() and StateEvent.objects.values('stop_code_id').order_by('-event_datetime').first() == Availability.objects.values('stop_code_id').order_by('-end_datetime').first():
        update_availability_object()
    else:
        create_availability_object()
