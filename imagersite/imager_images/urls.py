# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import LibraryView

# from . import views


urlpatterns = [
    url(r'^$', LibraryView.as_view(), name='library_view'),
]
