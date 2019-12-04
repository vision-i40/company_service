from django.test import TestCase
from django.dispatch import receiver
from django.db.models.signals import post_save
from company_service.models import Availability, Company, ProductionLine, StateEvent, CodeGroup, StopCode
from company_service.signals import create_availability_instance
from django.db.models import Q, Max, Min
import datetime
import pytz

class AvailabilitySignalTest(TestCase):
    def setUp(self):
        self.first_company = Company.objects.create(
            trade_name="company one",
            slug="c1",
            is_active=True)

        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="c1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=10200)

        self.first_code_group = CodeGroup.objects.create(
            company=self.first_company,
            name="group-test",
            group_type="Stop Code"
        )

        self.first_stop_code = StopCode.objects.create(
            company=self.first_company,
            is_planned=False,
            name="stop code test",
            code_group=self.first_code_group,
        )

        self.first_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        create_availability_instance(self.first_state_event)

        self.second_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 3, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        create_availability_instance(self.second_state_event)

        self.third_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

        create_availability_instance(self.third_state_event)

        self.fourth_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 8, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

        create_availability_instance(self.fourth_state_event)

        self.fifth_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 13, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        create_availability_instance(self.fifth_state_event)

        self.sixth_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 18, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        create_availability_instance(self.sixth_state_event)
    
    def signal_helper(self, state, stop_code_id):
        lower_datetime = Availability.objects.filter(Q(state=state) & Q(stop_code=stop_code_id)).aggregate(Min('start_time'))['start_time__min']
        higher_datetime = Availability.objects.filter(Q(state=state) & Q(stop_code=stop_code_id)).aggregate(Max('end_time'))['end_time__max']
        start_time = Availability.objects.filter(Q(state=state) & Q(stop_code=stop_code_id)).values('start_time').last()['start_time']
        end_time = Availability.objects.filter(Q(state=state) & Q(stop_code=stop_code_id)).values('end_time').last()['end_time']
        stop_code = Availability.objects.filter(Q(state=state) & Q(stop_code=stop_code_id)).values('stop_code').last()['stop_code']

        self.assertEqual(lower_datetime, start_time)
        self.assertEqual(higher_datetime, end_time)
        self.assertEqual(stop_code, stop_code_id)

    def test_to_see_if_the_events_with_state_off_and_same_stop_code_were_aggregated(self):
        self.signal_helper(StateEvent.OFF, self.first_stop_code.id)

    def test_to_see_if_the_events_with_state_on_were_aggregated(self):
        self.signal_helper(StateEvent.ON, None)