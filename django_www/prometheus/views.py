import os

from django.http import HttpResponse

from prometheus_client import CollectorRegistry, multiprocess, generate_latest
from prometheus_client import REGISTRY, CONTENT_TYPE_LATEST


def prometheus_view(request):

    if "prometheus_multiproc_dir" in os.environ:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = REGISTRY
    metrics_page = generate_latest(registry)
    return HttpResponse(metrics_page, content_type=CONTENT_TYPE_LATEST)
