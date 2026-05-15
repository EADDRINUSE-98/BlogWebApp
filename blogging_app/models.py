from django.db import models
from django.utils import timezone

# Create your models here.

IS_PUBLISHED_STATUS_CHOICE = {
    True: "Publish",
    False: "Draft",
}


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    publish_timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(
        default=False, max_length=7, choices=IS_PUBLISHED_STATUS_CHOICE
    )
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=150)
