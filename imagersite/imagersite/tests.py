# coding=utf-8
"""Test Module for ImagerSite."""
from django.test import TestCase
from imager_profile.models import User
from django.core.urlresolvers import resolve
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""

    class Meta:
        """Define a model instance class."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class AuthenticatedImageSiteTests(TestCase):
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
                                    {"username": "bob",
                                     "password": "wrongpassword"})
        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(response.status_code, 200)


class ImagerSiteTests(TestCase):
    """ImagerSite view and routing tests."""

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

    def test_home_view(self):
        """Test correct view is attached to correct URL."""
        resolver = resolve('/')
        self.assertEquals(resolver.view_name, 'home_page')

    def test_admin_view(self):
        """Test correct view is attached to correct URL."""
        resolver = resolve('/admin/')
        self.assertEquals(resolver.view_name, 'admin:index')
