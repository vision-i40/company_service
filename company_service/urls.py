from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import view as views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename="companies")

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^auth/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
