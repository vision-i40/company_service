from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Q
from . import serializers as serializers
from . import models as models


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        return models.Company \
            .objects \
            .filter(users=self.request.user) \
            .order_by('-created')

    def perform_create(self, serializer):
        company = serializer.save()

        company.users.add(self.request.user)


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UnitOfMeasurementSerializer

    def get_queryset(self):
        return models.UnitOfMeasurement \
            .objects \
            .filter(product__company__user=self.request.user, product=self.kwargs['products_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        product = models.Product \
            .objects \
            .get(company__user=self.request.user, pk=self.kwargs['products_pk'])
        serializer.save(product=product)


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.Product \
            .objects \
            .filter(company__users=self.request.user, company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=models.Company.objects.get(users=self.request.user, pk=self.kwargs['companies_pk']))


class ProductionLineViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductionLineSerializer

    def get_queryset(self):
        return models.ProductionLine \
            .objects \
            .filter(company__user=self.request.user, company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=models.Company.objects.get(users=self.request.user, pk=self.kwargs['companies_pk']))


class TurnSchemeViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TurnSchemeSerializer

    def get_queryset(self):
        return models.TurnScheme. \
            objects. \
            filter(company__user=self.request.user, company=self.kwargs['companies_pk']). \
            order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=models.Company.objects.get(users=self.request.user, pk=self.kwargs['companies_pk']))


class TurnViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TurnSerializer

    def get_queryset(self):
        return models.Turn \
            .objects \
            .filter(turn_scheme__company__user=self.request.user, turn_scheme=self.kwargs['turn_schemes_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        turn_scheme = models.TurnScheme \
            .objects \
            .get(company__user=self.request.user, pk=self.kwargs['turn_schemes_pk'])
        serializer.save(turn_scheme=turn_scheme)

class CodeGroupViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CodeGroupSerializer

    def get_queryset(self):
        return models.CodeGroup \
            .objects \
            .filter(company__user=self.request.user, company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=models.Company.objects.get(users=self.request.user, pk=self.kwargs['companies_pk']))

class StopCodeViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.StopCodeSerializer

    def get_queryset(self):
        return models.StopCode \
            .filter(code_group__company__user=self.request.user, code_group=self.kwargs['code_groups_pk']) \
            .objects \
            .order_by('-created')

    def perform_create(self, serializer):
        code_group = models.CodeGroup \
            .objects \
            .get(company__user=self.request.user, pk=self.kwargs['code_groups_pk'])
        serializer.save(code_group=code_group)

class WasteCodeViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.WasteCodeSerializer

    def get_queryset(self):
        return models.WasteCode \
            .objects \
            .filter(code_group__company__user=self.request.user, code_group=self.kwargs['code_groups_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        code_group = models.CodeGroup \
            .objects \
            .get(company__user=self.request.user, pk=self.kwargs['code_groups_pk'])
        serializer.save(code_group=code_group)

class ReworkCodeViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReworkCodeSerializer

    def get_queryset(self):
        return models.ReworkCode \
            .objects \
            .filter(code_group__company__user=self.request.user, code_group=self.kwargs['code_groups_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        code_group = models.CodeGroup \
            .objects \
            .get(company__user=self.request.user, pk=self.kwargs['code_groups_pk'])
        serializer.save(code_group=code_group)

class ProductionOrderViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductionOrderSerializer

    def get_queryset(self):
        return models.ProductionOrder \
            .objects \
            .filter(product__company__user=self.request.user, product__company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        product_id = serializer.validated_data['product_id']
        product = models.Product \
            .objects \
            .get(company__user=self.request.user, company=self.kwargs['companies_pk'], pk=product_id)
        serializer.save(product=product)

class ProductionEventViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductionEventSerializer

    def get_queryset(self):
        return models.ProductionEvent \
            .objects \
            .filter(company__user=self.request.user, product__company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        production_order = models.ProductionOrder \
            .objects \
            .get(
                company__user=self.request.user,
                company=self.kwargs['companies_pk'],
                pk=self.kwargs['production_orders_pk']
            )
        serializer.save(
            production_order=production_order,
            product=production_order.product
        )

class CollectorViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectorSerializer

    def get_queryset(self):
        return models.Collector \
            .objects \
            .filter(company__users=self.request.user, company=self.kwargs['companies_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        serializer.save(company=models.Company.objects.get(users=self.request.user, pk=self.kwargs['companies_pk']))

class ChannelViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ChannelSerializer

    def get_queryset(self):
        return models.Channel \
            .objects \
            .filter(collector__company__user=self.request.user, collector=self.kwargs['collectors_pk']) \
            .order_by('-created')

    def perform_create(self, serializer):
        collector = models.Collector \
            .objects \
            .get(
                company__user=self.request.user,
                pk=self.kwargs['collectors_pk']
            )
        serializer.save(collector=collector)