from behave import step
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


@step('I create a superuser with email "{email}" and password "{password}" and UUID "{user_uuid}"')
def create_superuser(context, email, password, user_uuid=None):
    get_user_model().objects.create_superuser(email=email, password=password, uuid=user_uuid)


@step('I create a user with email "{email}" and password "{password}"')
def create_user(context, email, password):
    get_user_model().objects.create_user(email=email, password=password)


@step('I create a group called "{group_name}"')
def create_group_request(context, group_name):
    Group.objects.create(name=group_name)


@step('I add the permission "{permission}" to the user email "{email}"')
def add_permission_to_user(context, permission, email):
    user = get_user_model().objects.get(email=email)
    permission = Permission.objects.get(codename=permission)
    user.user_permissions.add(permission)


@step('I add the permission "{permission}" to the group "{group_name}"')
def add_permission_to_group(context, permission, group_name):
    group = Group.objects.get(name="test_group")
    permission = Permission.objects.get(codename=permission)
    group.permissions.add(permission)


@step('I add the user "{email}" to the group "{group_name}"')
def step_impl(context, email, group_name):
    group = Group.objects.get(name="test_group")
    user = get_user_model().objects.get(email=email)
    user.groups.add(group)


@step('I create a user with email "{email}", password "{password}" and id "{id_user}"')
def create_user_with_id(context, email, password, id_user):
    get_user_model().objects.create_user(email=email, password=password, id=id_user)
