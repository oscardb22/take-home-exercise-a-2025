from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):

    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.authentication"
    verbose_name = _("Authentication and Authorization")
