from rest_framework.test import APIClient


def django_ready(context):
    context.test.client = APIClient()
