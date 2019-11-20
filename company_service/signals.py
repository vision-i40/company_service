from django.dispatch import receiver
from django.db.models.signals import post_save
from company_service.models import ManualStop, StateEvent

@receiver(post_save, sender=ManualStop)
def create_state_events(sender, **kwargs):
    manual_stop = ManualStop.objects
    if kwargs.get('created', True):
        if manual_stop.values('start_datetime'):
            StateEvent.objects.create(production_line_id=manual_stop.values('production_line_id').last()['production_line_id'], stop_code_id=manual_stop.values('stop_code_id').last()['stop_code_id'], event_datetime=manual_stop.values('start_datetime').last()['start_datetime'], state=StateEvent.OFF)
        if manual_stop.values('end_datetime'):
            StateEvent.objects.create(production_line_id=manual_stop.values('production_line_id').last()['production_line_id'], stop_code_id=manual_stop.values('stop_code_id').last()['stop_code_id'], event_datetime=manual_stop.values('end_datetime').last()['end_datetime'], state=StateEvent.OFF)