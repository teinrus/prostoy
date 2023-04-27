from django.apps import AppConfig
VERBOSE_APP_NAME = 'Простои'

class ProstoyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prostoy'
    verbose_name = VERBOSE_APP_NAME


