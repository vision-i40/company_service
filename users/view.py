from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], name='current')
    def current(self, request):
        serializer = self.get_serializer(request.user, many=False)
        return Response(serializer.data)
