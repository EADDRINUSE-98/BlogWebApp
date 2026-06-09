from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from time import time

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)
    counts = models.IntegerField()


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
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def save(self, *args, **kwargs):
        """
        This will override the save method to generate slug as per the title.
        Implement because, what if user changes the title of the post.
        """
        # if self.pk is None:
        if not self.slug:
            timestamp = str(int(time()))
        else:
            timestamp = self.slug.rsplit("-", 1)[-1]
        self.slug = f"{slugify(self.title)}-{timestamp}"
        super().save(*args, **kwargs)
