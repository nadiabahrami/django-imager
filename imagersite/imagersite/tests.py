# coding=utf-8
from django.test import TestCase


class ImagerSiteTests(TestCase):
    def setUp(self):
        from django.test import Client
        self.client = Client()

    def test_home(self):
        response = self.client.get("/home/", {})
        self.assertEquals(response.status_code, 200)

    def test_register(self):
        response = self.client.get("/accounts/register/", {})
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get("/accounts/login/", {})
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get("/accounts/logout/", {})
        self.assertEquals(response.status_code, 200)
