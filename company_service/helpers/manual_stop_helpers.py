from company_service.models import StateEvent, ManualStop

from company_service.helpers.common_helpers import create_object_of, get_attribute_from_the_last_object_of
from company_service import choices

def create_state_events_using(manual_stop_datetime):
    create_object_of(
        StateEvent,
        production_line_id=get_attribute_from_the_last_object_of(ManualStop, 'production_line_id')['production_line_id'],
        stop_code_id=get_attribute_from_the_last_object_of(ManualStop, 'stop_code_id')['stop_code_id'],
        event_datetime=manual_stop_datetime,
        state=choices.OFF
    )