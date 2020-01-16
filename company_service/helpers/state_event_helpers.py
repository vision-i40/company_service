from django.db.models import Q

from company_service.helpers.common_helpers import create_object_of, get_attribute_from_the_last_object_of
from company_service.models import Availability, StateEvent

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