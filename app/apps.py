from django.apps import AppConfig
from django.db import models


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = "Foreign words"

