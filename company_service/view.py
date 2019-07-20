from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers as serializers
from . import models as models

class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        return models.Company\
                        .objects\
                        .filter(user=self.request.user)\
                        .order_by('-updated_at')

    def perform_create(self, serializer):
        company = serializer.save()
        self.request.user.companies.add(company)

class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UnitOfMeasurementSerializer

    def get_queryset(self):
        return models.UnitOfMeasurement\
                        .objects\
                        .filter(company__user=self.request.user, company=self.kwargs['companies_pk'])\
                        .order_by('-updated_at')

class ProductionLineViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductionLineSerializer

    def get_queryset(self):
        return models.ProductionLine\
                        .objects\
                        .filter(company__user=self.request.user, company=self.kwargs['companies_pk'])\
                        .order_by('-updated_at')
