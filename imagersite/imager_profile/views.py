from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to imager profile page.  Make a profile or you know use and already established photo upload site.")
