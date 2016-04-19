# coding=utf-8
from django.test import TestCase
from imager_profile.models import User

import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""
    class Meta:
        """Define a model instance class."""
        model = User

    username = 'bob'
    email = 'bob@example.com'


class Authenticated_ImageSiteTests(TestCase):
    """Define a class with a series of profile tests."""

    def setUp(self):
        """Instance setup factory."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_login_post_valid(self):
        """Test if the user is in the DB, with valid login."""
        response = self.client.post("/accounts/login/",
                                    {"username": "bob", "password": "secret"})
        self.assertEquals(response.status_code, 302)

    def test_login_post_invalid(self):
        """Test if the user is in the DB, with invalid login."""
        response = self.client.post("/accounts/login/",
                                    {"username": "bob", "password": "wrongpassword"})
        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(response.status_code, 200)


class ImagerSiteTests(TestCase):
    def setUp(self):
        """Set up a default client."""
        from django.test import Client
        self.client = Client()

    def test_home(self):
        """Test that the home route is valid."""
        response = self.client.get("/", {})
        self.assertEquals(response.status_code, 200)

    def test_register(self):
        """Test that the register route is valid."""
        response = self.client.get("/accounts/register/", {})
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        """Test that the login route is valid."""
        response = self.client.get("/accounts/login/", {})
        self.assertEquals(response.status_code, 200)

    def test_login_post_invalid(self):
        """Test if a user is not in the DB, with invalid username."""
        response = self.client.post("/accounts/login/",
                                    {"username": "wrong", "password": ""})
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        """Test that the logout route is valid."""
        response = self.client.get("/accounts/logout/", {})
        self.assertEquals(response.status_code, 200)
