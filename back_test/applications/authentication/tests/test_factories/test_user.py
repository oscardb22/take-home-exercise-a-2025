from django.conf import settings
from django.utils import timezone
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

locale = getattr(settings, "LANGUAGE_CODE", "en_US")


class UserFactory(DjangoModelFactory):
    """docstring for UserFactory"""

    class Meta:
        model = "authentication.User"
        django_get_or_create = ("first_name", "last_name", "email", "password")

    first_name = Faker("name", locale=locale)
    last_name = Faker("name", locale=locale)
    email = Faker("email", locale=locale)
    password = Faker("password", locale=locale)
    is_superuser = True
    is_staff = True
    is_active = True
    date_joined = timezone.now()

    @post_generation
    def user_set_password(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            extracted.set_password(extracted.password)

    @post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
