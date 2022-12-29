from django.shortcuts import render
from django.http import HttpResponse


def second(request):
    return HttpResponse('this is my second fb view')
