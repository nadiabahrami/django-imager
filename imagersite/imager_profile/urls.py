# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import ProfileView

# from . import views

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile_view'),
]
