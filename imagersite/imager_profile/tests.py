"""Testing the image_profile models."""
from django.test import TestCase
import factory
from imager_profile.models import User, UserProfile


class ProfileTestCase2(TestCase):
    """Define a test case to see if testing works."""

    def setUp(self):
        """Set up a user named boo."""
        self.username = 'boo'

    def test_foo(self):
        """Assert username created and exits as boo."""
        self.assertEquals(self.username, 'boo')


class UserFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""

    class Meta:
        """Define a model instance class."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):
    """Define a class with a series of profile tests."""

    def setUp(self):
        """Instance setup factory."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_profile(self):
        """Test that profile is created on user save."""
        self.assertTrue(self.user.profile)

    def test_active(self):
        """Assert that .is_active is True."""
        self.assertTrue(self.user.is_active)

    def test_all_active(self):
        """Assert that the user profile is in the list or acitve profiles."""
        self.assertIn(self.user.profile, UserProfile.active.all())

    def test_all_active2(self):
        """All actives have a length of one."""
        self.assertEquals(len(UserProfile.active.all()), 1)

    def test_deactivate(self):
        """Assert that .is_active can be set to false correctly."""
        self.user.is_active = False
        self.assertFalse(self.user.is_active)

    def test_deactivate_later(self):
        """Test that non active users is not in all actives."""
        self.user.is_active = False
        self.user.save()
        self.assertNotIn(self.user.profile, UserProfile.active.all())


class DeleteTheDude(ProfileTestCase):
    """Define a class that deletes my bob."""

    def setUp(self):
        """Set up a factory of a deleted dude."""
        super(DeleteTheDude, self).setUp()
        self.user.delete()

    def test_all_active(self):
        """Test to see if bob is not in the active lists."""
        self.assertNotIn(self.user.profile, UserProfile.active.all())

    def test_all_active2(self):
        """Assert that there are no entries that are active."""
        self.assertEquals(len(UserProfile.active.all()), 0)
