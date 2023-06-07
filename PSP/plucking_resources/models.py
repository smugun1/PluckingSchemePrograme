from django.contrib.auth import admin
from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.
class Resources(models.Model):
    description = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/resources/')

    def __str__(self):
        return self.description


