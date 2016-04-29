from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from imager_api.serializer import PhotoSerializer
from imager_images.models import Photo
from rest_framework import permissions
from imager_api.permissions import IsOwner
from rest_framework.response import Response



class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.public.all().order_by('date_uploaded')
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,)

    def get_queryset(self):
        queryset = super(PhotoViewSet, self).get_queryset()

        user = self.request.user
        return queryset.filter(owner=user)


# class AlbumViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Album.all_albums.all()
#     serializer_class = AlbumSerializer