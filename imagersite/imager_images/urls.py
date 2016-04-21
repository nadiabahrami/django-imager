# -*- Coding:Utf-8 -*-
"""Module for my url routing."""
from django.conf.urls import url
from .views import LibraryView, AlbumView, PhotoView, add_photo, add_album, edit_album, edit_photo
from django.contrib.auth.decorators import login_required

# from . import views


urlpatterns = [
    url(r'^library/', login_required(LibraryView.as_view()), name='library_view'),
    url(r'^album/(?P<user_id>[0-9]+)/(?P<pk>[0-9]+)', login_required(AlbumView.as_view()), name='album_view'),
    url(r'^photos/(?P<user_id>[0-9]+)/(?P<pk>[0-9]+)', login_required(PhotoView.as_view()), name='photo_view'),
    url(r'^albums/add/', login_required(add_album), name='create_al_view'),
    url(r'^photos/add/', login_required(add_photo), name='add_pho_view'),
    url(r'^albums/(?P<pk>[0-9]+)/edit/', login_required(edit_album), name='create_al_view'),
    url(r'^photos/(?P<pk>[0-9]+)/edit/', login_required(edit_photo), name='add_pho_view'),
]
