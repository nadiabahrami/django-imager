from __future__ import unicode_literals
from imager_images.models import Photo, Album
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        user = self.request.user
        photo_count = Photo.public.filter(owner=user.pk).count()
        album_count = Album.all_albums.filter(owner=user.pk).count()
        return {'photo_count': photo_count, 'album_count': album_count}
