from __future__ import unicode_literals
from imager_images.models import Photo, Album
from imager_profile.models import UserProfile, EditProfile, EditUser
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User


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
        up = UserProfile.objects.get(user=request.user)
        form_profile = EditProfile(request.POST, instance=up)
        u = User.objects.get(profile=up)
        form_user = EditUser(request.POST, instance=u)
        if form_profile.is_valid() and form_user.is_valid():
            form_profile.instance.user = request.user
            form_user.instance.user = request.user
            form_profile.save()
            form_user.save()
            return HttpResponseRedirect('/profile/')
        return render(request, 'edit_profile.html', context={'form_profile': form_profile,  'form_user': form_user})
    else:
        up = UserProfile.objects.get(user=request.user)
        form_profile = EditProfile(instance=up)
        u = User.objects.get(profile=up)
        form_user = EditUser(instance=u)
        return render(request, 'edit_profile.html', context={'form_profile': form_profile, 'form_user': form_user})
