"""Testing the imager_images models."""
from django.test import TestCase
import factory
from imager_images.models import Photo, Album
from imager_profile.models import User
from datetime import datetime


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

        self.album1 = Album.all_albums.create(title='album1', owner=self.user)
        self.album1.save()

        self.image1 = Photo.public.create(title='image1', owner=self.user)
        self.image1.save()

        self.album1.pictures.add(self.image1)

    def test_album(self):
        """Test that album manager connection is made."""
        self.assertTrue(self.user.album)

    def test_album_title(self):
        """Test album title is correct and created."""
        self.assertEquals(self.album1.title, 'album1')

    def test_album_description(self):
        """Test that album description is created."""
        self.assertEquals(self.album1.description, '')

    def test_album_owner(self):
        """Test that album owner is connected to correct user."""
        self.assertEquals(self.album1.owner.username, 'bob')

    def test_album_publish_status(self):
        """Test that published status is default of private."""
        self.assertEquals(self.album1.published, 'private')

    def test_album_date_created(self):
        """Test that album has a datetime object in published date."""
        self.assertIsInstance(self.album1.date_created, datetime)

    def test_album_date_modified(self):
        """Test that has a datetime object in modified date."""
        self.assertIsInstance(self.album1.date_modified, datetime)

    def test_album_date_published(self):
        """Test that album does not have a pblished date."""
        self.assertIsNone(self.album1.date_published)

    def test_album_pictures(self):
        """Test that album picture containes picture manager connection."""
        self.assertIsNotNone(self.album1.pictures)

    def test_photo(self):
        """Test that photo manager connection is made."""
        self.assertTrue(self.user.photo)

    def test_photo_title(self):
        """Test photo title is correct and created."""
        self.assertEquals(self.image1.title, 'image1')

    def test_photo_description(self):
        """Test that photo description is created."""
        self.assertEquals(self.image1.description, '')

    def test_photo_owner(self):
        """Test that album owner is connected to correct user."""
        self.assertEquals(self.image1.owner.username, 'bob')

    def test_photo_publish_status(self):
        """Test that published status is default of private."""
        self.assertEquals(self.image1.published, 'private')

    def test_photo_date_uploaded(self):
        """Test that photo has a datetime object in published date."""
        self.assertIsInstance(self.image1.date_uploaded, datetime)

    def test_photo_date_modified(self):
        """Test that has a datetime object in modified date."""
        self.assertIsInstance(self.image1.date_modified, datetime)

    def test_photo_date_published(self):
        """Test that album does not have a pblished date."""
        self.assertIsNone(self.image1.date_published)
