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
        # for each in Photo.public.all():
        #     print(each)
        random_photo_url = Photo.public.filter(published__contains='public').order_by("?")[:1]
        # random_photo_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
        return {'random_photo': random_photo_url[0].photo_file}