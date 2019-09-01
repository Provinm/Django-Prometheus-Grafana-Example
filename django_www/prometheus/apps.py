from django.apps import AppConfig

from .server import start_server


class PrometheusConfig(AppConfig):
    name = "prometheus"

    def ready(self):

        start_server()
        super(PrometheusConfig, self).ready()
