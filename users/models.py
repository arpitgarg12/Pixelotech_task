from django.db import models

# Create your models here.

class User(models.Model):
    mobile = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)


class Image(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=20)