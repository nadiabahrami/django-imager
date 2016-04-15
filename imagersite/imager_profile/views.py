from __future__ import unicode_literals
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from imager_profile.models import UserProfile
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        """Return a random public photo for homepage."""
        # c = super(, self).get_context_data(**kwargs)
        user = self.request.user
        # return c
        photo_count = Photo.public.filter(owner=user.pk).count()
        # album_count = Album.public.all(owner=user.pk).count()
        return {'photo_count': photo_count}
# , 'album_count': album_count



# def get_context_data(request, profile_id=None, **kwargs):
#        """Return a random public photo for homepage."""
#        photo_count = Photo.public.filter(id=int(profile_id)).count()
#        # album_count = Album.public.all(owner__contains=self.request.user).count()
#        return {'photo_count': photo_count,} # 'album_count': album_count}
    # album_count = Album.public.all(owner__contains=self.request.user).count()
    # return render(request, "profile.html", context={'photo_count': photo_count,}) # 'album_count': album_count}



    # def profile_view(request, profile_id=None, **kwargs):
    #     if not profile_id:
    #         profile = request.user.profile
    #     else:
    #         profile = get_object_or_404(ImagerProfile, id=int(profile_id))
    #
    #     return render(request, "profile.html", context={"profile": profile})