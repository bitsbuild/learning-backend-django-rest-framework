from django.db import models
import uuid
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
class StreamingPlatform(models.Model):
    platform_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    platform_name = models.CharField(max_length=70)
    platform_about = models.CharField(max_length=350)
    platform_url = models.URLField()
class ContentDetails(models.Model):
    content_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    content_name = models.CharField(max_length=70)
    content_description = models.CharField(max_length=350)
    content_released = models.BooleanField(default=True)
    content_created = models.DateTimeField(auto_now_add=True,editable=False)
    content_updated = models.DateTimeField(default=timezone.now,editable=True)
class ContentReviews(models.Model):
    review_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    review_name = models.CharField(max_length=70)
    review_body = models.CharField(max_length=350)
    review_stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_created = models.DateTimeField(auto_now_add=True,editable=False)
    review_updated = models.DateTimeField(default=timezone.now,editable=True)
class Artists(models.Model):
    artist_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    artist_name = models.CharField(max_length=70)
    artist_about = models.CharField(max_length=350)