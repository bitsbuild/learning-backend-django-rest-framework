from django.db import models
import uuid
# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=250)
    isReleased = models.BooleanField(default=True)
    reviews = models.JSONField(default=list)
    cast = models.JSONField(default=list)

    def __str__(self):
        return self.name