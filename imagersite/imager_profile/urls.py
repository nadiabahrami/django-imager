# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import ProfileView
from django.contrib.auth.decorators import login_required

# from . import views

urlpatterns = [
    url(r'^$', login_required(ProfileView.as_view()), name='profile_view'),
]
