from rest_framework import serializers

from company_service.serializers import ProductionOrderSerializer
from .models import ProductionChart

class ProductionChartSerializer(serializers.HyperlinkedModelSerializer):
    event_type = serializers.CharField(write_only=True)
    production_order = ProductionOrderSerializer(read_only=True)

    production_line_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    class Meta:
        model = ProductionChart
        fields = (
            'id',
            'production_order',
            'production_line_id',
            'product_id',
            'start_datetime',
            'end_datetime',
            'quantity',
            'event_type'
        )

class RejectChartSerializer(ProductionChartSerializer):
    event_type = serializers.CharField()
    class Meta(ProductionChartSerializer.Meta):
        model = ProductionChart
        fields = (
            ProductionChartSerializer.Meta.fields + ('event_type',)
        )