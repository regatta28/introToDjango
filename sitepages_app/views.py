# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return HttpResponse('Test This site!')
def home(request):
    return HttpResponse('Test Home')

def about(request):
    return HttpResponse('Test about')
def contact(request):
    return HttpResponse('Test contact')
# Create your views here.
