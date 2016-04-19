from django.db import models
# from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


PHOTO_ACCESS_CHOICES = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('shared', 'Shared'),
)


def _image_path(instance, filename):
    """Photo will be uploaded to media root then correct folder."""
    return "user_{0}/{1}".format(instance.owner.id, filename)


class PhotoManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(PhotoManager, self).get_queryset()
        return qs.all()

    # def get_queryset(self):
    #     """Return a list of all active users."""
    #     qs = super(ActiveProfileManager, self).get_queryset()
    #     return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class Photo(models.Model):
    """Create photos for a user."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="photo")
    photo_file = models.ImageField(upload_to=_image_path)
    title = models.CharField(max_length=30, blank=True, null=True)
                             # default=photo_file.filename)
    description = models.CharField(max_length=60, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(max_length=30, choices=PHOTO_ACCESS_CHOICES,
                                 default='private')
    public = PhotoManager()

    def __str__(self):
        """Return the ownership and name of photo."""
        return "{}'s photo of {}".format(self.owner.username, self.title)


class AlbumManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(AlbumManager, self).get_queryset()
        return qs.all()


@python_2_unicode_compatible
class Album(models.Model):
    """Define album class."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="album")
    pictures = models.ManyToManyField(Photo, related_name="pictures")
    cover = models.ForeignKey(Photo, related_name="cover_of", blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)
    published = models.CharField(max_length=30, choices=PHOTO_ACCESS_CHOICES,
                                 default='private')
    all_albums = AlbumManager()

    def __str__(self):
        """Return the user's album name."""
        return "{}'s album of {}".format(self.owner.username, self.title)
