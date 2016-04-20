# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import LibraryView, AlbumView, PhotoView, AddPhoto, CreateAlbum
from django.contrib.auth.decorators import login_required

# from . import views


urlpatterns = [
    url(r'^library/', login_required(LibraryView.as_view()), name='library_view'),
    url(r'^album/(?P<user_id>[0-9])/(?P<pk>[0-9])', login_required(AlbumView.as_view()), name='album_view'),
    url(r'^photos/(?P<user_id>[0-9])/(?P<pk>[0-9])', login_required(PhotoView.as_view()), name='photo_view'),
    url(r'^albums/add/)', login_required(CreateAlbum.as_view()), name='create_al_view'),
    url(r'^photos/add/)', login_required(AddPhoto.as_view()), name='add_pho_view'),
]
