from django.shortcuts import render

from django.htpp import HttpResponse

def index(request):
    return HttpResponse("hello")
# Create your views here.
