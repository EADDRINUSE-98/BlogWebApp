from django.db import models

# Create your models here.


class Post(models.Models):
    title = models.CharField(max_length=30)
    publish_timestamp = models.DataTimeField()
