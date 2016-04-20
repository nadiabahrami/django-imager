from __future__ import unicode_literals
from django.views.generic.detail import DetailView
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


class AlbumView(DetailView):
    template_name = 'album.html'

    model = Album

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        context = super(AlbumView, self).get_context_data(**kwargs)
        return context


class PhotoView(DetailView):
    template_name = 'photos.html'

    model = Photo

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        context = super(PhotoView, self).get_context_data(**kwargs)
        return context
