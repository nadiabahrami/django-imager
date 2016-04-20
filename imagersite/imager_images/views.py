from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.detail import DetailView
from imager_images.models import Photo, Album, CreateAlbum, AddPhoto
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


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


def add_album(request):
    form = CreateAlbum(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return render(request, 'create_album.html', context={'form': form})


def add_photo(request):
    form = AddPhoto(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return render(request, 'add_photo.html', context={'form': form})

