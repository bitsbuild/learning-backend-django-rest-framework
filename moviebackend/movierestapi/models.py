from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    description = models.CharField(max_length=250)
    isReleased = models.BooleanField(default=True)
    reviews = models.JSONField(default=list)
    cast = models.JSONField(default=list)

    def __str__(self):
        return self.name