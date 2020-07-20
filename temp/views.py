from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse("Buffer Hub")