from django.core.signals import request_started
from django.dispatch import receiver

from .metrics import req_counter


@receiver(request_started)
def incr_request(sender, **kw):

    req_counter.inc(1)
