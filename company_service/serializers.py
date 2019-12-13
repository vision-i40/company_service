from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from typing import Dict, Any

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'trade_name',
            'slug',
            'corporate_name',
            'cnpj',
            'email',
            'phone',
            'address',
            'zip_code',
            'neighborhood',
            'city',
            'state',
            'country',
            'industrial_sector',
            'size',
            'is_active',
            'created',
            'modified',
        )


class UnitOfMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = (
            'id',
            'name',
            'is_default',
            'conversion_factor',
            'created',
            'modified',
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    units_of_measurement = UnitOfMeasurementSerializer(many=True, source='unitofmeasurement_set', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'company_id',
            'name',
            'units_of_measurement',
            'created',
            'modified',
        )


class ProductionOrderSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    product_id = serializers.IntegerField(required=True)
    production_line_id = serializers.IntegerField(required=False)

    production_quantity = serializers.IntegerField(required=False)
    waste_quantity = serializers.IntegerField(required=False)
    rework_quantity = serializers.IntegerField(required=False)
    stop_quantity = serializers.ReadOnlyField()

    class Meta:
        model = ProductionOrder
        fields = (
            'id',
            'product',
            'product_id',
            'production_line_id',
            'code',
            'state',
            'production_quantity',
            'waste_quantity',
            'rework_quantity',
            'stop_quantity',
            'quantity',
            'created',
            'modified',
        )

class TurnSchemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TurnScheme
        fields = (
            'id',
            'company_id',
            'name',
            'created',
            'modified'
        )


class TurnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turn
        fields = (
            'id',
            'turn_scheme_id',
            'name',
            'start_time',
            'end_time',
            'days_of_week',
            'created',
            'modified'
        )

class ProductionLineSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = ProductionLine
            fields = (
                'id',
                'company_id',
                'name',
                'is_active',
                'discount_rework',
                'discount_waste',
                'stop_on_production_absence',
                'time_to_consider_absence',
                'reset_production_changing_order',
                'micro_stop_seconds',
                'created',
                'modified'
            )

class ProductionLineWithOrderAndTurnSerializer(WritableNestedModelSerializer, ProductionLineSerializer):
    in_progress_order = ProductionOrderSerializer(read_only=True)
    current_turn = TurnSerializer(read_only=True)

    class Meta(ProductionLineSerializer.Meta):
        model = ProductionLine
        fields = (
            ProductionLineSerializer.Meta.fields + ('in_progress_order', 'current_turn')
        )


class CodeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodeGroup
        fields = (
            'id',
            'company_id',
            'name',
            'group_type',
            'created',
            'modified'
        )

class StopCodeSerializer(serializers.HyperlinkedModelSerializer):
    code_group = CodeGroupSerializer(read_only=True)

    class Meta:
        model = StopCode
        fields = (
            'id',
            'company_id',
            'is_planned',
            'name',
            'code_group',
            'created',
            'modified'
        )

class WasteCodeSerializer(serializers.HyperlinkedModelSerializer):
    code_group = CodeGroupSerializer(read_only=True)

    class Meta:
        model = WasteCode
        fields = (
            'id',
            'company_id',
            'name',
            'code_group',
            'created',
            'modified'
        )

class ReworkCodeSerializer(serializers.HyperlinkedModelSerializer):
    code_group = CodeGroupSerializer(read_only=True)

    class Meta:
        model = ReworkCode
        fields = (
            'id',
            'company_id',
            'name',
            'code_group',
            'created',
            'modified'
        )

class ProductionEventSerializer(serializers.HyperlinkedModelSerializer):
    production_order = ProductionOrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    unit_of_measurement = UnitOfMeasurementSerializer(read_only=True)

    production_line_id = serializers.IntegerField(required=True)

    rework_code = ReworkCodeSerializer(read_only=True)
    waste_code = WasteCodeSerializer(read_only=True)

    class Meta:
        model = ProductionEvent
        fields = (
            'id',
            'product',
            'production_line_id',
            'production_order',
            'unit_of_measurement',
            'event_datetime',
            'quantity',
            'event_type',
            'waste_code',
            'rework_code',
            'created',
            'modified',
        )

class CollectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collector
        fields = (
            'id',
            'created',
            'modified',
            'mac',
            'collector_type',
        )

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    production_line = ProductionLineSerializer(read_only=True)

    production_line_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Channel
        fields = (
            'id',
            'created',
            'modified',
            'number',
            'channel_type',
            'inverse_state',
            'is_cumulative',
            'production_line',
            'production_line_id',
        )

class StateEventSerializer(serializers.HyperlinkedModelSerializer):
    channel = ChannelSerializer(read_only=True)
    stop_code = StopCodeSerializer(read_only=True)

    channel_id = serializers.IntegerField(required=False)
    stop_code_id = serializers.IntegerField(required=False)
    availability_id = serializers.IntegerField()
    class Meta:
        model = StateEvent
        fields = (
            'id',
            'channel',
            'channel_id',
            'stop_code',
            'stop_code_id',
            'availability_id',
            'event_datetime',
            'state',
            'created',
            'modified',
        )

class ManualStopSerializer(serializers.HyperlinkedModelSerializer):
    stop_code = StopCodeSerializer(read_only=True)

    stop_code_id = serializers.IntegerField()
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    state = serializers.CharField(read_only=True)
    class Meta:
        model = ManualStop
        fields = (
            'id',
            'stop_code',
            'stop_code_id',
            'start_datetime',
            'end_datetime',
            'state',
            'created',
            'modified',
        )

class AvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    production_line = ProductionLineSerializer(read_only=True)
    stop_code = StopCodeSerializer(read_only=True)

    start_datetime = serializers.DateTimeField(required=False)
    end_datetime = serializers.DateTimeField(required=False)
    state = serializers.CharField(required=False)
    class Meta:
        model = Availability
        fields = (
            'id',
            'production_line',
            'start_datetime',
            'end_datetime',
            'stop_code',
            'state',
        )

class ProductionChartSerializer(serializers.HyperlinkedModelSerializer):
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField(allow_null=True)

    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductionChart
        fields = (
            'id',
            'product',
            'start_datetime',
            'end_datetime',
            'quantity',
        )

class ProductionLineStopSerializer(AvailabilitySerializer):
    class Meta(AvailabilitySerializer.Meta):
        model = Availability
        fields = (
            AvailabilitySerializer.Meta.fields
        )

