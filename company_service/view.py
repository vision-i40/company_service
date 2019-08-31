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
            .filter(users=self.request.user)\
            .order_by('-created')

    def perform_create(self, serializer):
        company = serializer.save()

        company.users.add(self.request.user)


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UnitOfMeasurementSerializer

    def get_queryset(self):
        return models.UnitOfMeasurement\
            .objects\
            .filter(product__company__user=self.request.user, product=self.kwargs['product_pk'])\
            .order_by('-created')

    def perform_create(self, serializer):
        product = models.Product\
            .objects\
            .get(company__user=self.request.user, pk=self.kwargs['product_pk'])
        serializer.save(product=product)


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.Product\
            .objects\
            .filter(company__user=self.request.user, company=self.kwargs['companies_pk'])\
            .order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.companies.get(pk=self.kwargs['companies_pk']))


class ProductConversionViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductConversionSerializer

    def get_queryset(self):
        return models.ProductConversion\
            .objects\
            .filter(product__company__user=self.request.user, product__company=self.kwargs['companies_pk'])\
            .order_by('-created')


class ProductionLineViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductionLineSerializer

    def get_queryset(self):
        return models.ProductionLine\
            .objects\
            .filter(company__user=self.request.user, company=self.kwargs['companies_pk'])\
            .order_by('-created')
