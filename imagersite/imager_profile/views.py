from __future__ import unicode_literals
from imager_images.models import Photo, Album
from imager_profile.models import UserProfile, EditProfile
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
        u = UserProfile.objects.get(user=request.user)
        form_profile = EditProfile(request.POST, instance=u)
        if form_profile.is_valid():
            form_profile.instance.user = request.user
            form_profile.save()
            return HttpResponseRedirect('/profile/')
        return render(request, 'edit_profile.html', context={'form_profile': form_profile})
    else:
        u = UserProfile.objects.get(user=request.user)
        form_profile = EditProfile(instance=u)
        return render(request, 'edit_profile.html', context={'form_profile': form_profile})


# def update_settings(request):
#     if request.method== 'POST':
#         u = UserProfile.objects.get(user=request.user)
#         form = UserProfile(request.POST, instance=u)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return HttpResponseRedirect('/profile/')
#         return render(request, 'edit_profile.html', context={'form_profile': form_profile})
#     else:
#         u = UserProfile.objects.get(user=request.user)
#         form = UserProfileForm(instance=u) #No request.POST
#         return render(request, 'edit_profile.html', context={'form_profile': form_profile})