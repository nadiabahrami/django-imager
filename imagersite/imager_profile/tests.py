from django.test import TestCase

# Create your tests here.

class ProfileTestCase(TestCase):

    def setUp(self):
        self.username = 'boo'

    def test_foo(self):
        self.assertEquals(self.username, 'boo')
