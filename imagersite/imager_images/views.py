from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
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
    form.fields['pictures'].queryset = request.user.photo
    form.fields['cover'].queryset = request.user.photo
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect('/images/library/')
    return render(request, 'create_album.html', context={'form': form})


# TODO: From class notes, Selena
# def get_object(self, queryset=None)
# try:
#     return super(AddOrEditContent, self).get_object(queryset)
# except AttributeError:
#     return

def edit_album(request, pk):
    # TODO: Finish this form
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        try:
            user_album = Album.all_albums.get(id=pk)
            form = CreateAlbum(request.POST, instance=user_album)
        except ObjectDoesNotExist:
            form = CreateAlbum(request.POST, request.FILES)
            form.fields['pictures'].queryset = request.user.photo
            form.fields['cover'].queryset = request.user.photo

        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect('/images/library/')
    else:
        try:
            user_album = Album.all_albums.get(id=pk)
            form = CreateAlbum(request.POST, instance=user_album)
            form.fields['pictures'].queryset = request.user.photo
            form.fields['cover'].queryset = request.user.photo
        except ObjectDoesNotExist:
            form = CreateAlbum(request.POST, request.FILES)
            form.fields['pictures'].queryset = request.user.photo
            form.fields['cover'].queryset = request.user.photo
        return render(request, 'edit_album.html', context={'form': form})


def add_photo(request):
    form = AddPhoto(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect('/library/')
    return render(request, 'add_photo.html', context={'form': form})


def edit_photo(request):
    form = AddPhoto(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return render(request, 'edit_photo.html', context={'form': form})