from loguru import logger
from rest_framework import status

from applications.authentication.models import User
from applications.authentication.tests.test_factories.test_user import UserFactory
from back_test.utils.base_test import BaseTestCase


class UserViewTestCase(BaseTestCase):
    """docstring UserViewTestCase"""

    def setUp(self):
        self.user = self.create_user()
        self.create_login()
        self.url = "/api/v1/authentication/users/"

    def test_list_groups(self):
        logger.info(" test_list_groups ")
        UserFactory.create()
        response = self.client.get(self.url)
        self.validate_http_status(response, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)
        self.assertIsInstance(response.data, dict)

    def test_set_new_password_wrong(self):
        url = self.url + "set-new-password/"
        data = {"new_password": "new_pas", "old_password": "old_password"}
        response = self.client.post(url, data=data)
        self.validate_http_status(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["errors"][0]["msgs"][0], "Wrong current password"
        )
