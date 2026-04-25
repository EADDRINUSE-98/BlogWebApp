from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    publish_timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    content = models.TextField()
