from django.shortcuts import render
from django.http.response import HttpResponse


def test_response(request):
    return HttpResponse('faza')