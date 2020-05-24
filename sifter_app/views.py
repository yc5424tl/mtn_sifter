from django.shortcuts import render
from logging import Logger
from django.http import JsonResponse
from http import HTTPStatus


def stay_alive(request):
    if request.method == "GET":
        return JsonResponse(data={'stay': 'alive'}, status=HTTPStatus.OK)



