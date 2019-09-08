from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from users.models import User
from common.models import IndexedTimeStampedModel
from django.contrib.postgres.fields import ArrayField


class Company(IndexedTimeStampedModel):
    trade_name = models.CharField(max_length=256)
    corporate_name = models.CharField(max_length=256, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    email = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    zip_code = models.CharField(max_length=256, blank=True)
    neighborhood = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    industrial_sector = models.CharField(max_length=256, blank=True)
    size = models.CharField(max_length=256, blank=True)
    slug = models.SlugField(db_index=True)
    is_active = models.BooleanField(default=False)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.trade_name

class Product(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class UnitOfMeasurement(IndexedTimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    is_default = models.BooleanField(default=False)
    conversion_factor = models.FloatField(default=1.0)

    def __str__(self):
        return self.name

class CodeGroup(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    group_type = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class StopCode(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class WasteCode(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)


class ReworkCode(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    code_group = models.ForeignKey(CodeGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)


class TurnScheme(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Turn(IndexedTimeStampedModel):
    turn_scheme = models.ForeignKey(TurnScheme, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=256)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = ArrayField(
        models.IntegerField(),
        default=list,
    )

    def __str__(self):
        return self.name


class ProductionLine(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    discount_rework = models.BooleanField(default=False)
    discount_waste = models.BooleanField(default=False)
    stop_on_production_absence = models.BooleanField(default=False)
    time_to_consider_absence = models.IntegerField(blank=True, null=True)
    reset_production_changing_order = models.BooleanField(default=False)
    micro_stop_seconds = models.IntegerField(blank=True, null=True)
    turn_scheme = models.ForeignKey(TurnScheme, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class StopEvent(IndexedTimeStampedModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    stop_code = models.ForeignKey(StopCode, on_delete=models.SET_NULL, null=True)


class WasteEvent(IndexedTimeStampedModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    waste_code = models.ForeignKey(WasteCode, on_delete=models.SET_NULL, null=True)


class ReworkEvent(IndexedTimeStampedModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    rework_code = models.ForeignKey(ReworkCode, on_delete=models.SET_NULL, null=True)


class ProductionOrder(IndexedTimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=256)
    state = models.CharField(max_length=256)


class ProductionLineProductionRate(IndexedTimeStampedModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.FloatField()


class Collector(IndexedTimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mac = models.CharField(max_length=256)
    collectorType = models.CharField(max_length=256)


class Channel(IndexedTimeStampedModel):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE)
    production_line = models.ForeignKey(ProductionLine, blank=True, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField()
    channelType = models.CharField(max_length=256)
    inverse_state = models.BooleanField(default=False)
    is_cumulative = models.BooleanField(default=False)
