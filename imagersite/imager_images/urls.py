# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]