from django.shortcuts import HttpResponse


def index(requests):

    return HttpResponse("hello, world")
