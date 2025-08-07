from django.contrib.auth import authenticate

from applications.authentication.tests.test_factories.test_user import UserFactory
from back_test.utils.base_test import BaseTestCase


class UserTestCase(BaseTestCase):

    def setUp(self):
        self.user = self.create_user()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(email=self.user_email, password=self.user_password)
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(email=f"w{self.user_email}", password=self.user_password)
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(email=self.user_email, password=f"w{self.user_password}")
        self.assertFalse(user is not None and user.is_authenticated)
