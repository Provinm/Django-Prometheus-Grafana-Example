from django.conf.urls import url
from .views import prometheus_view

urlpatterns = [
    url(r'^metrics$', prometheus_view, name='prometheus-metrics'),
]
