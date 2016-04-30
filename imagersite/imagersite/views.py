# -*- coding:utf-8 -*-
"""Imagersite views created."""
from __future__ import unicode_literals
from django.views.generic import TemplateView
from imager_images.models import Photo


class HomeView(TemplateView):
    """Define the ClassView class."""

    template_name = 'home.html'

    def get_context_data(self):
        """Return a random public photo for homepage."""
        try:
            random_photo = Photo.public.filter(published__contains='public').order_by("?")[:1][0]
        except IndexError:
            random_photo = False
        return {'random_photo': random_photo}
