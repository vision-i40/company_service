from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, default=None)
    is_active = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)