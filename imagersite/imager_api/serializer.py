from django.contrib.auth.models import User, Group
from rest_framework import serializers
from imager_images.models import Photo, Album



class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Photo
        fields = ('owner', 'photo_file', 'title', 'description', 'date_uploaded',
                  'date_modified', 'date_published', 'published')


# class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Album
#         fields = ('owner', 'pictures', 'cover', 'title', 'description', 
#                   'date_created', 'date_modified', 'date_published', 'published')