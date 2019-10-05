from rest_framework import serializers
from .models import User
from company_service.serializers import CompanySerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    default_company = CompanySerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'is_active',
            'default_company',
            'created',
            'modified',
        )
