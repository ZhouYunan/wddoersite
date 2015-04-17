from django.db import models
from django.http import HttpResponse
from django.views.generic import TemplateView



def login(request):
    return HttpResponse('hello')
