from rest_framework import serializers
from .models import Group
from company_service.serializers import CompanySerializer

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    default_company = CompanySerializer()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'default_company',
            'permissions',
            'created',
            'modified',
        )