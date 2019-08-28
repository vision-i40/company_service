from rest_framework import viewsets, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from . import models as models

@api_view(['GET'])
@authentication_classes([JWTAuthentication,])
@permission_classes((IsAuthenticated,))
def get_user_profile(request):
    return Response({
        'profile': {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
            'is_active': request.user.is_active,
            'created': request.user.created,
            'modified': request.user.modified,
        },
        'selected_company': {
            'name': 'A Name',
            'slug': 1,
        }
    })
