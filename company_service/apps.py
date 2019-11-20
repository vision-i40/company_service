from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CompanyServiceConfig(AppConfig):
    name = 'company_service'

    def ready(self):
        import company_service.signals #noqa
    