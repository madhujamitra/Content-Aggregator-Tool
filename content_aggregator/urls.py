from django.contrib import admin
from django.urls import path, include

from content_aggregator.core.views import aggregation_list_view, aggregation_detail_view, error_404, home_view, extract

urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('aggregations/', aggregation_list_view, name='aggregation_list'),
    path('aggregations/<int:pk>/', aggregation_detail_view, name='aggregation_detail'),
    path('aggregations/<int:pk>/', error_404, name='error_404'),
    path('extract/', extract, name='extract'),
]