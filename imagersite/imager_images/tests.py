"""Testing the imager_images models."""
from django.test import TestCase
import factory
from imager_images.models import Photo, Album, CreateAlbum, AddPhoto
from imager_profile.models import User, UserProfile


class UserFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""

    class Meta:
        """Define a model instance class."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ImageTestCase(TestCase):
    """Define a class with a series of image tests."""

    def setUp(self):
        """Instance setup factory."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

        self.album_1 = Album(title='album 1', owner=self.user)
        self.album_2 = Album(title='album 2', owner=self.user)
        self.album_1.save()
        self.album_2.save()

        self.image_1 = Photo(title='image 1', owner=self.user)
        self.image_2 = Photo(title='image 2', owner=self.user)
        self.image_1.save()
        self.image_2.save()

        self.album_1.pictures.add(self.image_1)
        self.album_1.pictures.add(self.image_2)

        self.album_2.pictures.add(self.image_2)


    def test_album(self):
        """Test that profile is created on user save."""
        self.assertTrue(self.user.album)


##### leverage the following NOTES for testing forms ###
# from rebar.testing import flatten_to_dict
# from contacts import forms
# ...
# class EditContactFormTests(TestCase):

#     def test_mismatch_email_is_invalid(self):

#         form_data = flatten_to_dict(forms.ContactForm())
#         form_data['first_name'] = 'Foo'
#         form_data['last_name'] = 'Bar'
#         form_data['email'] = 'foo@example.com'
#         form_data['confirm_email'] = 'bar@example.com'

#         bound_form = forms.ContactForm(data=form_data)
#         self.assertFalse(bound_form.is_valid())

#     def test_same_email_is_valid(self):

#         form_data = flatten_to_dict(forms.ContactForm())
#         form_data['first_name'] = 'Foo'
#         form_data['last_name'] = 'Bar'
#         form_data['email'] = 'foo@example.com'
#         form_data['confirm_email'] = 'foo@example.com'

#         bound_form = forms.ContactForm(data=form_data)
#         self.assert_(bound_form.is_valid())