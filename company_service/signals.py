from django.dispatch import receiver
from django.db.models.signals import post_save
from company_service.models import ManualStop, StateEvent, Availability
from django.db.models import Q, Min, Max

@receiver(post_save, sender=ManualStop)
def create_state_events(sender, **kwargs):
    manual_stop = ManualStop.objects
    start_datetime = manual_stop.values('start_datetime').last()['start_datetime']
    end_datetime = manual_stop.values('end_datetime').last()['end_datetime']
    def set_state_events(datetime):
        StateEvent.objects.create(production_line_id=manual_stop.values('production_line_id').last()['production_line_id'],
                stop_code_id=manual_stop.values('stop_code_id').last()['stop_code_id'],
                event_datetime=datetime,
                state=StateEvent.OFF)

    if kwargs.get('created', True):
        if manual_stop.values('start_datetime'):
            set_state_events(start_datetime)
        if manual_stop.values('end_datetime'):
            set_state_events(end_datetime)
