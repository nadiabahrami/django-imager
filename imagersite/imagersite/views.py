# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader
from django.views.generic import TemplateView
from imager_images.models import Photo
from registration.backends.simple.views import RegistrationView
# from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        """Return a random public photo for homepage."""
        try:
            random_photo = Photo.public.filter(published__contains='public').order_by("?")[:1][0]
        except IndexError:
            random_photo = False
        return {'random_photo': random_photo}


# class MyRegistrationView(RegistrationView):
#     def get_success_url(self, request, user):
#         return "/home/"