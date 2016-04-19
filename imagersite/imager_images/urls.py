# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import LibraryView
from django.contrib.auth.decorators import login_required

# from . import views


urlpatterns = [
    url(r'^$', login_required(LibraryView.as_view()), name='library_view'),
]
