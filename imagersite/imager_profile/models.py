# -*- Coding:Utf-8 -*-
"""Define Imager Profile models."""
from django.db import models

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        ga = super(ActiveProfileManager, self).get_queryset()
        return ga.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class UserProfile(models.Model):
    """Create a unique profile for a user."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        primary_key=True,
    )
    camera_type = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=60, blank=True)
    web_link = models.CharField(max_length=70, blank=True)
    photo_type = models.CharField(max_length=30, blank=True)
    social_media = models.CharField(max_length=30, blank=True)

    active = ActiveProfileManager()

    @property
    def is_active(self):
        """Property to define if user is active."""
        return self.user.is_active
