from django.conf.urls import url

from .views import AvailabilityChartViewSet, ProductionChartViewSet, RejectChartViewSet

urlpatterns = [
    url(r'^availability_chart/$', AvailabilityChartViewSet.as_view({'get': 'list'}), name='availability_chart'),
    url(r'^production_chart/$', ProductionChartViewSet.as_view({'get': 'list'}), name='production_chart'),
    url(r'^reject_chart/$', RejectChartViewSet.as_view({'get': 'list'}), name='reject_chart'),
]