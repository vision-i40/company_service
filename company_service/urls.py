from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_nested import routers
from . import view as views

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

router = routers.SimpleRouter()
router.register('companies', views.CompanyViewSet, basename="companies")

companies_router = routers.NestedSimpleRouter(router, 'companies', lookup='companies')
companies_router.register('production_lines', views.ProductionLineViewSet, base_name='companies-production_lines')
companies_router.register('products', views.ProductViewSet, base_name='companies-products')

products_router = routers.NestedSimpleRouter(companies_router, 'products', lookup='products')
products_router.register('units_of_measurement', views.UnitOfMeasurementViewSet,
                         base_name='companies-products-units_of_measurement')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^v1/', include(companies_router.urls)),
    url(r'^v1/', include(products_router.urls)),
    url(r'^auth/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
