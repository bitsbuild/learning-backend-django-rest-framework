from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    isReleased = models.BooleanField(default=True)
    reviews = models.JSONField(default=list)
    cast = models.JSONField(default=list)
