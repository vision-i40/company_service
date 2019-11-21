from django.dispatch import receiver
from django.db.models.signals import post_save
from company_service.models import ManualStop, StateEvent, Availability

@receiver(post_save, sender=ManualStop)
def create_state_events(sender, **kwargs):
    manual_stop = ManualStop.objects
    if kwargs.get('created', True):
        if manual_stop.values('start_datetime'):
            StateEvent.objects.create(production_line_id=manual_stop.values('production_line_id').last()['production_line_id'], 
                                        stop_code_id=manual_stop.values('stop_code_id').last()['stop_code_id'], 
                                        event_datetime=manual_stop.values('start_datetime').last()['start_datetime'], 
                                        state=StateEvent.OFF)
        if manual_stop.values('end_datetime'):
            StateEvent.objects.create(production_line_id=manual_stop.values('production_line_id').last()['production_line_id'], 
                                        stop_code_id=manual_stop.values('stop_code_id').last()['stop_code_id'], 
                                        event_datetime=manual_stop.values('end_datetime').last()['end_datetime'], 
                                        state=StateEvent.OFF)

@receiver(post_save, sender=StateEvent)
def create_availability_instance(sender, **kwargs):
    state_event = StateEvent.objects
    if kwargs.get('created', True):
        # if StateEvent.objects.values('state').last()['state'] == StateEvent.ON :
        Availability.objects.create(production_line_id=state_event.values('production_line_id').last()['production_line_id'], 
                                        start_time=state_event.values('event_datetime').earliest('event_datetime')['event_datetime'], 
                                        end_time=state_event.values('event_datetime').latest('event_datetime')['event_datetime'], 
                                        stop_code_id=state_event.values('stop_code_id').last()['stop_code_id'],
                                        state=state_event.values('state').last()['state'])
        # elif StateEvent.objects.values('state').last()['state'] == StateEvent.OFF:

            