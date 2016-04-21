# -*- Coding:Utf-8 -*-
"""Define Imager Profile models."""
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.forms import ModelForm


class ActiveProfileManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


LOCATION = (
    ('North America', 'North America'),
    ('Asia', 'Asia'),
    ('Africa', 'Africa'),
    ('South America', 'South America'),
    ('Europe', 'Europe'),
)


@python_2_unicode_compatible
class UserProfile(models.Model):
    """Create a unique profile for a user."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        primary_key=True,
    )
    camera_type = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=60, blank=True)
    web_link = models.CharField(max_length=70, blank=True)
    photo_type = models.CharField(max_length=30, blank=True)
    social_media = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, choices=LOCATION,
                              default='North America')

    friends = models.ManyToManyField("self", symmetrical=False,
                                     related_name='friend_of')
    objects = models.Manager()
    active = ActiveProfileManager()

    @property
    def is_active(self):
        """Property to define if user is active."""
        return self.user.is_active

    def __str__(self):
        """Hand back username's profile."""
        return "{}'s profile".format(self.user.username)


class EditUser(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfile(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['camera_type', 'address', 'web_link', 'photo_type', 'social_media', 'region']
