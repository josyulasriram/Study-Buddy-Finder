from django.apps import AppConfig


class SbuddyConfig(AppConfig):
    name = 'sbuddy'
    def ready(self):
        import sbuddy.signals

