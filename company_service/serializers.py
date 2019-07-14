from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

class ProductionLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'is_active', 'oee_goal', 'discount_rework', 'discount_waste', 'stop_on_production_abscence', 'created_at', 'updated_at')