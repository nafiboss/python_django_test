from django.db import models

class Topic(models.Model):
    group = models.CharField(max_length=256)
    description = models.TextField()
    image_url = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    guid = models.CharField(max_length=256, primary_key=True)

