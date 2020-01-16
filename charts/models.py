from django.db import models

from common.models import DateTimedEvent, IndexedTimeStampedModel
from company_service.models import (ProductionLine, ProductionOrder, 
                                    Product, ProductionEvent)

class ProductionChart(DateTimedEvent, IndexedTimeStampedModel):
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    event_type = models.CharField(max_length=20, choices=ProductionEvent.EVENT_TYPES, default=ProductionEvent.PRODUCTION, db_index=True)
