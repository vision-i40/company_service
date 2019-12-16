from django.test import TestCase
from company_service.models import Availability, Company, ProductionLine, StateEvent, CodeGroup, StopCode
from django.db.models import Q, Max, Min

import datetime
import pytz

class AvailabilityModelTest(TestCase):
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

        self.first_availability_instance = Availability.objects.create(
            production_line=self.first_production_line,
        )

        self.second_availability_instance = Availability.objects.create(
            production_line=self.first_production_line,
        )

        self.first_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            availability=self.first_availability_instance,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        self.second_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            availability=self.first_availability_instance,
            channel=None,
            stop_code=None,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 3, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.ON
        )

        self.third_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            availability=self.second_availability_instance,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

        self.fourth_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            availability=self.second_availability_instance,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 12, 50, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

        self.fifth_state_event = StateEvent.objects.create(
            production_line=self.first_production_line,
            availability=self.second_availability_instance,
            channel=None,
            stop_code=self.first_stop_code,
            event_datetime=datetime.datetime(2019, 12, 3, 13, 30, 54, 988870, tzinfo=pytz.UTC),
            state=StateEvent.OFF
        )

    def availability_aggregation_helper(self, availability_instance, first_event, last_event):
        start_datetime = availability_instance.start_datetime()
        end_datetime = availability_instance.end_datetime()
        state = availability_instance.state()
        stop_code_id = availability_instance.stop_code_id()

        self.assertEqual(first_event.event_datetime, start_datetime)
        self.assertEqual(last_event.event_datetime, end_datetime)
        self.assertEqual(last_event.state, state)
        if StateEvent.state == 'Off':
            self.assertEqual(last_event.stop_code.id, stop_code_id)

    def test_availability_instance_aggregation(self):
        self.availability_aggregation_helper(self.first_availability_instance, self.first_state_event, self.second_state_event)
        self.availability_aggregation_helper(self.second_availability_instance, self.third_state_event, self.fifth_state_event)
