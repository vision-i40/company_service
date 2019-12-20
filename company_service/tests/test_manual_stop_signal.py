from django.test import TestCase
from company_service.models import ManualStop, StateEvent, ProductionLine, StopCode, CodeGroup, Company, ProductionLineStop

import datetime
import pytz

class ManualStopSignalTestCase(TestCase):
    def setUp(self):
        self.first_company = Company.objects.create(
            trade_name="company one",
            slug="c1",
            is_active=True)

        self.first_production_line = ProductionLine.objects.create(
            company=self.first_company,
            name="pl1",
            is_active=True,
            discount_rework=True,
            discount_waste=True,
            stop_on_production_absence=True,
            time_to_consider_absence=True,
            reset_production_changing_order=True,
            micro_stop_seconds=15800)

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

        self.first_manual_stop = ManualStop.objects.create(
            production_line=self.first_production_line,
            start_datetime=datetime.datetime(2019, 12, 3, 11, 3, 55, 988870, tzinfo=pytz.UTC),
            end_datetime=datetime.datetime(2019, 12, 3, 12, 3, 55, 988870, tzinfo=pytz.UTC),
            stop_code=self.first_stop_code
        )

    def test_to_see_if_the_state_events_were_created_through_manual_stop(self):
        self.assertEqual(StateEvent.objects.count(), 2)

    def test_to_check_if_were_created_a_stop_instance_through_manual_stop(self):
        self.assertEqual(ProductionLineStop.objects.count(), 1)

    def test_to_check_if_the_stop_instance_created_returned_with_is_manual_flag_true(self):
        self.assertTrue(ProductionLineStop.objects.values('is_manual'))
