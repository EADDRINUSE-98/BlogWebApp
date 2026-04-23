from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

"""
test.py -

Covers:

How to run:
./manage.py test
"""


class HomeViewTest(TestCase):
    """Tests for testing home view."""

    def setUp(self):
        self.client = Client()

    def test_return_200(self):
        """Must return 200 status when hit base url."""
        response = self.client.get(reverse("blogging_app:home"))
        self.assertEqual(response.status_code, 200)
