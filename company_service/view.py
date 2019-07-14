from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer, ProductionLineSerializer
from . import models as models

class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer

    def get_queryset(self):
        return models.Company\
                        .objects\
                        .filter(user=self.request.user)\
                        .order_by('-updated_at')

class ProductionLineViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductionLineSerializer

    def get_queryset(self):
        return models.ProductionLine\
                        .objects\
                        .filter(company__user=self.request.user, company=self.kwargs['company_pk'])\
                        .order_by('-updated_at')