from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'is_active', 'created_at', 'updated_at')