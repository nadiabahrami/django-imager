from __future__ import unicode_literals
from imager_images.models import Photo, Album
from imager_profile.models import UserProfile
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        user = self.request.user
        photo_count = Photo.public.filter(owner=user.pk).count()
        album_count = Album.all_albums.filter(owner=user.pk).count()
        return {'photo_count': photo_count, 'album_count': album_count}


def edit_profile(request):
    if request.method == 'POST':
        # user_album = UserProfile.all_albums.get()
        # form = CreateAlbum(request.POST, instance=user_album)
        # if form.is_valid():
        #     form.instance.owner = request.user
        #     form.save()
        #     return HttpResponseRedirect('/profile/')
        # return render(request, 'edit_album.html', context={'form': form})
        pass
    else:
        user = UserProfile.objects.get(user=request.user)
        form_profile = UserProfile(instance=user)
        return render(request, 'edit_profile.html', context={'form_profile': form_profile})