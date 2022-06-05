from django.apps import AppConfig

class RegistrationConfig(AppConfig):
    name = 'registration'

class BbsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bbs'