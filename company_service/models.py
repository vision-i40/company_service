from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class ProductionLine(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    oee_goal = models.FloatField()
    discount_rework = models.BooleanField(default=False)
    discount_waste = models.BooleanField(default=False)
    stop_on_production_abscence = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)