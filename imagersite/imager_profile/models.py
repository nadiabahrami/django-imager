from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile = models.ForeignKey(User, unique=True)
    camera_type = models.CharField(('nikkon'), max_length=30, blank=True)
    address = models.CharField(('address'), max_length=60, blank=True)
    web_link = models.CharField(('personal site'), max_length=70, blank=True)
    photo_type = models.CharField(('nature'), max_length=30, blank=True)
    social_media = models.CharField(('handle'), max_length=30, blank=True)

    @property
    def is_active(self):
        return self.user.is_active
    