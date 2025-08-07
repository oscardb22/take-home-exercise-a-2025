from django.contrib.auth import get_user_model
from django.test import Client, TestCase, TransactionTestCase
from jsonschema import validate
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase, TestCase, TransactionTestCase):
    """
    docstring for BaseTestCase
    """

    serialized_rollback = True
    client = Client()
    url = None
    user_email = "admin@admin.com"
    user_password = "12346ASDFASDasdfa*"
    """def setUp(self):
        setUp docstring
        perms = Permission.objects.all().values_list("id", flat=True)
        for g in Group.objects.all():
            g.permissions.add(*perms)"""

    def create_user(self):
        """docstring for method create_user"""
        return get_user_model().objects.create_superuser(
            email=self.user_email, password=self.user_password
        )

    def create_login(self):
        """create_token docstring"""
        self.client.login(username=self.user_email, password=self.user_password)

    @staticmethod
    def assert_valid_schema(data, schema):
        """Checks whether the given data matches the schema"""
        return validate(data, schema)

    def pagination_validation(self, data_json):
        """pagination_validation assert"""
        self.assertTrue("count" in data_json, "Not found this field count")
        self.assertTrue("next" in data_json, "Not found this field next")
        self.assertTrue("previous" in data_json, "Not found this field previous")
        self.assertTrue("results" in data_json, "Not found this field results")
        self.assertTrue(len(data_json["results"]) > 0, "The result list is empty")

    def validate_http_status(self, response, status_code):
        """validate_http_status assert"""
        self.assertEqual(
            response.status_code,
            status_code,
            f"The current http {response.status_code} status code "
            f"is different of {status_code}",
        )
