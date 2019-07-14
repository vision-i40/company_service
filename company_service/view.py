from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer
from . import models as models


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer

    def get_queryset(self):
        return models.Company.objects.filter(user=self.request.user).order_by('-updated_at')