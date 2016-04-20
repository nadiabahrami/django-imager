from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, make an imager_profile if you have never heard of a place called Flicker.")