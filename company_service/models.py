from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

class BaseModel(models.Model):
    created = AutoCreatedField(_('created'), db_index=True)
    modified = AutoLastModifiedField(_('modified'), db_index=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, db_index=True)
    is_active = models.BooleanField(default=False)


class Product(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    production_rate_per_hour = models.FloatField()
    description = models.TextField(default=None, blank=True, null=True)


class UnitOfMeasurement(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    conversion_factor = models.FloatField()
    is_global = models.BooleanField(default=False)
    description = models.TextField(default=None, blank=True, null=True)


class ProductConversion(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE)
    conversion_factor = models.FloatField()


class CodeGroup(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    groupType = models.CharField(max_length=256)


class StopCode(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)


class WasteCode(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)


class ReworkCode(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)


class TurnScheme(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)


class Turn(BaseModel):
    turn_scheme = models.ForeignKey(TurnScheme, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    start_time = models.TimeField()
    end_time = models.TimeField()


class ProductionLine(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    oee_goal = models.FloatField(blank=True, null=True)
    discount_rework = models.BooleanField(default=False)
    discount_waste = models.BooleanField(default=False)
    stop_on_production_abscence = models.BooleanField(default=False)
    turn_scheme = models.ForeignKey(TurnScheme, blank=True, null=True, on_delete=models.SET_NULL)


class StopEvent(BaseModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    stop_code = models.ForeignKey(StopCode, on_delete=models.SET_NULL, null=True)


class WasteEvent(BaseModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    waste_code = models.ForeignKey(WasteCode, on_delete=models.SET_NULL, null=True)


class ReworkEvent(BaseModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    rework_code = models.ForeignKey(ReworkCode, on_delete=models.SET_NULL, null=True)


class ProductionOrder(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=256)
    state = models.CharField(max_length=256)


class ProductionLineProductionRate(BaseModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.FloatField()


class Collector(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mac = models.CharField(max_length=256)
    collectorType = models.CharField(max_length=256)


class Channel(BaseModel):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE)
    production_line = models.ForeignKey(ProductionLine, blank=True, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField()
    channelType = models.CharField(max_length=256)
    inverse_state = models.BooleanField(default=False)
    is_cumulative = models.BooleanField(default=False)
