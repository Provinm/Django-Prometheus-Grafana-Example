from prometheus_client import start_http_server
from django.conf import settings


PROM_PORT = getattr(settings, "PROMETHEUS_PORT", 3001)
PROM_ADDR = getattr(settings, "PROMETHEUS_ADDR", "")


def start_server():

    start_http_server(port=PROM_PORT, addr=PROM_ADDR)
