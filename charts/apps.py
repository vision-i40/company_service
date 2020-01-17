from django.apps import AppConfig


class ChartsConfig(AppConfig):
    name = 'charts'

    def ready(self):
        import charts.signals #noqa
