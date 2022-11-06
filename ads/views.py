from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)
