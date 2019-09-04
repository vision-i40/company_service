from .models import *
from rest_framework import serializers


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


class ProductionLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductionLine
        fields = (
            'id',
            'company_id',
            'name',
            'is_active',
            'oee_goal',
            'discount_rework',
            'discount_waste',
            'stop_on_production_abscence',
            'created',
            'modified'
        )
