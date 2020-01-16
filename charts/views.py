from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from company_service.models import Company
from company_service.view import AvailabilityViewSet
from company_service import choices
from . import models

from .serializers import ProductionChartSerializer, RejectChartSerializer

class AvailabilityChartViewSet(AvailabilityViewSet):
    def get_queryset(self):
        return super().get_queryset().filter(state=choices.OFF)

class ProductionChartViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductionChartSerializer

    def get_queryset(self):
        return models.ProductionChart \
            .objects \
            .filter(production_order__production_line__company__user=self.request.user, production_order__production_line__company=self.kwargs['companies_pk'], event_type=models.ProductionEvent.PRODUCTION) \
            .order_by('-end_datetime')

class RejectChartViewSet(ProductionChartViewSet):
    serializer_class = RejectChartSerializer

    def get_queryset(self):
        return models.ProductionChart \
            .objects \
            .filter(production_order__production_line__company__user=self.request.user, production_order__production_line__company=self.kwargs['companies_pk']) \
            .filter(Q(event_type=models.ProductionEvent.WASTE) | Q(event_type=models.ProductionEvent.REWORK)) \
            .order_by('-end_datetime')
