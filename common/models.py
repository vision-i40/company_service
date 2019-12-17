
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class IndexedTimeStampedModel(models.Model):
    created = AutoCreatedField(_('created'), db_index=True)
    modified = AutoLastModifiedField(_('modified'), db_index=True)

    class Meta:
        abstract = True

class DateTimedEvent(models.Model):
    start_datetime = models.DateTimeField(default=None, db_index=True, null=True, blank=True)
    end_datetime = models.DateTimeField(default=None, db_index=True, null=True, blank=True)

    class Meta:
        abstract = True
