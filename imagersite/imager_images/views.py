from __future__ import unicode_literals
from imager_images.models import Photo, Album
from django.views.generic import TemplateView


class LibraryView(TemplateView):
    template_name = 'library.html'

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        user = self.request.user
        imgs = Photo.public.filter(owner=user.pk)
        albums = Album.all_albums.filter(owner=user.pk)
        return {'imgs': imgs, 'albums': albums}
