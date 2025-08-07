import hashlib

from behave import step


def _helper_set_headers(context):
    # TODO change to use headers on Django 4.2, remove HTTP_ prefix
    headers = {
        "HTTP_Content-Type": "application/json",
        "HTTP_Accept": "application/json",
    }
    if hasattr(context, "headers"):
        headers |= context.headers
    return headers


@step('I make a GET request to "{url}"')
def get_request_url(context, url):
    # TODO change to use headers on Django 4.2
    headers = _helper_set_headers(context)
    context.response = context.test.client.get(url, **headers)


@step('I make a POST request to "{url}" with')
def post_request_url(context, url):
    # TODO change to use headers on Django 4.2
    headers = _helper_set_headers(context)
    context.response = context.test.client.post(
        path=url, data=context.text, content_type="application/json", **headers
    )


@step('I login with "{email}" and password "{password}"')
def login_user(context, email, password):
    login_valid = context.test.client.login(email=email, password=password)
    context.test.assertTrue(login_valid)


@step('I set a custom header called "{header}" with encrypted SHA256 value "{value}"')
def custom_header_sha_256(context, header, value):
    if not hasattr(context, "headers"):
        context.headers = dict()
    encrypted_data = hashlib.sha256(value.encode()).hexdigest()
    # TODO change to use headers on Django 4.2,  remove HTTP_ prefix
    context.headers["HTTP_" + header] = encrypted_data


@step('I set a custom header called "{header}" with value "{value}"')
def custom_header(context, header, value):
    if not hasattr(context, "headers"):
        context.headers = dict()
    # TODO change to use headers on Django 4.2,  remove HTTP_ prefix
    context.headers["HTTP_" + header] = value
