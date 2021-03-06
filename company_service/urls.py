from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_nested import routers
from . import view as views
from users.view import UserViewSet
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

router = routers.SimpleRouter()
router.register('companies', views.CompanyViewSet, basename="companies")
router.register('users', UserViewSet, basename='users')

companies_router = routers.NestedSimpleRouter(router, 'companies', lookup='companies')
companies_router.register('production_lines', views.ProductionLineViewSet, basename='companies-production_lines')
companies_router.register('products', views.ProductViewSet, basename='companies-products')
companies_router.register('turn_schemes', views.TurnSchemeViewSet, basename='companies-turn_schemes')
companies_router.register('code_groups', views.CodeGroupViewSet, basename='companies-code_groups')
companies_router.register('production_orders', views.ProductionOrderViewSet, basename='production_orders')
companies_router.register('collectors', views.CollectorViewSet, basename='companies-collectors')
companies_router.register('availability', views.AvailabilityViewSet, basename='companies-availability')

products_router = routers.NestedSimpleRouter(companies_router, 'products', lookup='products')
products_router.register('units_of_measurement', views.UnitOfMeasurementViewSet,
                         basename='companies-products-units_of_measurement')

turn_schemes_router = routers.NestedSimpleRouter(companies_router, 'turn_schemes', lookup='turn_schemes')
turn_schemes_router.register(r'turns', views.TurnViewSet, basename='companies-turn_schemes-turns')

code_group_router = routers.NestedSimpleRouter(companies_router, 'code_groups', lookup='code_groups')
code_group_router.register('stop_codes', views.StopCodeViewSet, basename='companies-code_groups-stop_codes')
code_group_router.register('waste_codes', views.WasteCodeViewSet, basename='companies-code_groups-waste_codes')
code_group_router.register('rework_codes', views.ReworkCodeViewSet, basename='companies-code_groups-rework_codes')

production_line_router = routers.NestedSimpleRouter(companies_router, 'production_lines', lookup='production_lines')
production_line_router.register('state_events', views.StateEventViewSet, basename='companies-production_lines-state_events')
production_line_router.register('manual_stops', views.ManualStopViewSet, basename='companies-production_lines-manual_stops')
production_line_router.register('stops', views.ProductionLineStopsViewSet, basename='companies-production_lines-stops')
production_line_router.register('pending_stops', views.ProductionLinePendingStopsViewSet, basename='companies-production_lines-pending_stops')

production_order_router = routers.NestedSimpleRouter(companies_router, 'production_orders', lookup='production_orders')
production_order_router.register('production_events', views.ProductionEventViewSet, basename='companies-production_orders-production_events')

collectors_router = routers.NestedSimpleRouter(companies_router, 'collectors', lookup='collectors')
collectors_router.register('channels', views.ChannelViewSet, basename='companies-collectors-channels')

swagger_view = get_schema_view(
    title='Docs',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    url(r'^docs/$', swagger_view),
    url(r'^v1/', include(router.urls)),
    url(r'^v1/', include(companies_router.urls)),
    url(r'^v1/', include(products_router.urls)),
    url(r'^v1/', include(turn_schemes_router.urls)),
    url(r'^v1/', include(code_group_router.urls)),
    url(r'^v1/', include(production_order_router.urls)),
    url(r'^v1/', include(production_line_router.urls)),
    url(r'^v1/', include(collectors_router.urls)),
    url(r'^v1/companies/(?P<companies_pk>\d+)/charts/', include(('charts.urls', 'charts'), namespace='charts')),
    url(r'^auth/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
