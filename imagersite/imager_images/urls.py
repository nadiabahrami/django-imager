# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import LibraryView, AlbumView, PhotoView
from django.contrib.auth.decorators import login_required

# from . import views


urlpatterns = [
    url(r'^library/', login_required(LibraryView.as_view()), name='library_view'),
    url(r'^album/(?P<user_id>[0-9])/(?P<pk>[0-9])', login_required(AlbumView.as_view()), name='album_view'),
    url(r'^photos/(?P<user_id>[0-9])/(?P<pk>[0-9])', login_required(PhotoView.as_view()), name='photo_view'),
]
