from django.test import TestCase
import factory
from imager_profile.models import User

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