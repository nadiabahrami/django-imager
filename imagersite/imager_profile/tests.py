from django.test import TestCase
import factory
from imager_profile.models import User, UserProfile

# Create your tests here.

class ProfileTestCase2(TestCase):

    def setUp(self):
        self.username = 'boo'

    def test_foo(self):
        self.assertEquals(self.username, 'boo')



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob'
    email = 'bob@example.com'



class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_profile(self):
        self.assertTrue(self.user.profile)

    def test_active(self):
        self.assertTrue(self.user.is_active)

    def test_all_active(self):
        self.assertIn(self.user.profile, UserProfile.active.all())

    def test_all_active2(self):
        self.assertEquals(len(UserProfile.active.all()), 1)

    def test_deactivate(self):
        self.user.is_active = False
        self.assertFalse(self.user.is_active)

    def test_deactivate_later(self):
        self.user.is_active = False
        self.user.save()
        self.assertNotIn(self.user.profile, UserProfile.active.all())


class DeleteTheDude(ProfileTestCase):

    def setUp(self):
        super(DeleteTheDude, self).setUp()
        self.user.delete()

    def test_all_active(self):
        self.assertNotIn(self.user.profile, UserProfile.active.all())

    def test_all_active2(self):
        self.assertEquals(len(UserProfile.active.all()), 0)