from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile, TemporaryUploadedFile
from blogging_app.logic.image_processor import image_processing, image_saver
import os
import subprocess

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


class FileUploadTest(TestCase):
    """Tests the image upload feature"""

    def test_InMemoryUploadedFile(self):
        """Must return (True, None)"""
        with open("/data/images/foo.png", "rb") as img:
            image_name = "foo.png"
            image_content = img.read()
            content_type = "image/png"
            uploaded_file = SimpleUploadedFile(image_name, image_content, content_type)
            approved, reason, extension = image_processing(uploaded_file)
        self.assertTrue(approved)
        self.assertIsNone(reason)
        self.assertEqual(extension, "png")

    def test_TemporaryUploadedFile(self):
        """Must return (True, None)"""
        with TemporaryUploadedFile(
            "foo.png", "image/png", os.path.getsize("/data/images/foo.png"), "utf-8"
        ) as tmp:
            with open("/data/images/foo.png", "rb") as img:
                tmp.write(img.read())
            tmp.seek(0)
            approved, reason, extension = image_processing(tmp)
        self.assertTrue(approved)
        self.assertIsNone(reason)
        self.assertEqual(extension, "png")

    def test_image_saver(self):
        """Must not return False"""
        with open("/data/images/foo.png", "rb") as img:
            image_name = "foo.png"
            image_content = img.read()
            content_type = "image/png"
            uploaded_file = SimpleUploadedFile(image_name, image_content, content_type)
            success, file_name = image_saver(uploaded_file, "png")
        self.assertNotEqual(success, False)
        if os.path.exists(f"/data/images/{file_name}"):
            subprocess.run(["rm", f"/data/images/{file_name}"])
