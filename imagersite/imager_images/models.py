from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


PHOTO_ACCESS_CHOICES = (
    ('public', 'public'),
    ('private', 'private'),
    ('shared', 'shared'),
)

 # "Users should be able to designate one contained photo as the ‘cover’ for the album. """


@python_2_unicode_compatible
class Photo(models.Model):
    """Create photos for a user."""

    owner = models.ForeignKey(User, related_name="photo")
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=60, blank=True)
    photo_file = models.ImageField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(max_length=30, choices=PHOTO_ACCESS_CHOICES,
                                 default='private')


@python_2_unicode_compatible
class Album(models.Model):
    """Define album class."""
    owner = models.ForeignKey(User, related_name="album")
    pictures = models.ManyToManyField(Photo, related_name="pictures")
    cover = models.ForeignKey(Photo, related_name="cover")
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=60, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(max_length=30, choices=PHOTO_ACCESS_CHOICES,
                                 default='private')
