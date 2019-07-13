from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from common.models import IndexedTimeStampedModel
from django.db import models
from .managers import UserManager
from company_service.models import Company

class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    companies = models.ManyToManyField(Company)

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=256)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
