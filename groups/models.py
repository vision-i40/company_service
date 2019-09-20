from django.db import models
from django.contrib.auth.models import Permission
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from common.models import IndexedTimeStampedModel
# from users.models import User

class Group(IndexedTimeStampedModel):
    name = models.CharField(max_length=150)
    permissions = models.ManyToManyField(Permission, 'group_permissions')
    users = models.ManyToManyField('users.User')
    default_company = models.ForeignKey('company_service.Company', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
