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

# @receiver(post_save, sender=StateEvent)
# def create_availability_instance(sender, **kwargs):
#     state_event = StateEvent.objects
#     availability = Availability.objects
#     def set_availability_instance(state, start_datetime, end_datetime):
#         Availability.objects.create(production_line_id=state_event.values('production_line_id').last()['production_line_id'],
#                                 start_time=start_datetime,
#                                 end_time=end_datetime,
#                                 stop_code_id=state_event.values('stop_code_id').last()['stop_code_id'],
#                                 state=state)

#     def aggregate_availability_instances(state):
#         state_event_stop_code = state_event.values('stop_code_id').last()['stop_code_id']

#         higher_state_event_time = state_event.filter(Q(state=state) & Q(stop_code_id=state_event_stop_code)).values('event_datetime').aggregate(Max('event_datetime'))['event_datetime__max']
#         lower_state_event_time = state_event.filter(Q(state=state) & Q(stop_code_id=state_event_stop_code)).values('event_datetime').aggregate(Min('event_datetime'))['event_datetime__min']

#         set_availability_instance(state, lower_state_event_time, higher_state_event_time)
#         availability.filter(Q(start_time=lower_state_event_time) & Q(end_time__lt=higher_state_event_time)).delete()

#     if kwargs.get('created', True):
#         if StateEvent.objects.values('state').last()['state'] == StateEvent.ON:
#             aggregate_availability_instances(StateEvent.ON)
#         elif StateEvent.objects.values('state').last()['state'] == StateEvent.OFF:
#             aggregate_availability_instances(StateEvent.OFF)
