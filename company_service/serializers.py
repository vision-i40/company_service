from .models import *
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'slug',
            'is_active',
            'created',
            'modified'
        )


class UnitOfMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = (
            'id',
            'company_id',
            'name',
            'conversion_factor',
            'is_global',
            'created',
            'modified'
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'company_id',
            'name',
            'description',
            'production_rate_per_hour',
            'created',
            'modified'
        )


class ProductConversionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductConversion
        fields = (
            'id',
            'product_id',
            'unitofmeasurement_id',
            'conversion_factor',
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
            'oee_goal',
            'discount_rework',
            'discount_waste',
            'stop_on_production_abscence',
            'created',
            'modified'
        )
