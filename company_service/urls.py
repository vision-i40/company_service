from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_nested import routers
from . import view as views

from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

router = routers.SimpleRouter()
router.register(r'companies', views.CompanyViewSet, basename="companies")

companies_router = routers.NestedSimpleRouter(router, r'companies', lookup='companies')
companies_router.register(r'production_lines', views.ProductionLineViewSet, base_name='companies-production_lines')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^v1/', include(companies_router.urls)),
    url(r'^auth/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
