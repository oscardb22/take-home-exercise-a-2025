import uuid as uuid_lib

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CommonInfo(models.Model):
    """docstring for CommonInfo"""

    id = models.BigAutoField(
        primary_key=True,
        editable=False,
        db_column="id",
    )
    uuid = models.UUIDField(
        verbose_name=_("uuid"),
        db_column="uuid",
        default=uuid_lib.uuid4,
        db_index=True,
        unique=True,
        editable=False,
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        db_column="created_at",
        db_index=True,
        help_text=_("Created at"),
    )

    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        null=True,
        blank=True,
        db_column="updated_at",
        help_text=_("Updated at"),
    )

    deleted_at = models.DateTimeField(
        _("Deleted at"),
        null=True,
        blank=True,
        db_column="deleted_at",
        help_text=_("Deleted at"),
    )

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """docstring for UserManager"""

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError(_("The given email must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given email, and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(
        primary_key=True,
        editable=False,
        db_column="id",
    )
    uuid = models.UUIDField(
        verbose_name=_("uuid"),
        db_column="uuid",
        default=uuid_lib.uuid4,
        unique=True,
        editable=False,
    )
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_("first name"), max_length=150, blank=True
    )
    last_name = models.CharField(
        verbose_name=_("last name"), max_length=150, blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    picture_profile = models.ImageField(upload_to="images/", null=True, blank=True)
    file_info = models.FileField(upload_to="docs/", null=True, blank=True)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = f"{str(self.first_name).title()} {str(self.last_name).title()}"
        return full_name.strip()

    def get_short_name(self):
        return str(self.first_name).title()

    class Meta:
        app_label = "authentication"
        db_table = "authentication_users"
        ordering = ["email"]
        verbose_name = _("user")
        verbose_name_plural = _("users")
