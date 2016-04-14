# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.views.generic import TemplateView
from imager_images.models import Photo


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        """Return a random public photo for homepage."""
        # for each in Photo.public.all():
        #     print(each)
        try:
            random_photo = Photo.public.filter(published__contains='public').order_by("?")[:1][0]
        except IndexError:
            random_photo = False
        return {'random_photo': random_photo}
