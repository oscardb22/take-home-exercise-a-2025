import logging

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import Http404, JsonResponse
from rest_framework import exceptions as rest_exceptions
from rest_framework import views as rest_views
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class GeneralErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, exception):
        # Log unmanaged errors
        logger.exception(
            f"An unmanaged error occurred on lss, error details: {exception}"
        )

        # Return a simple error response
        error_message = (
            f"An unmanaged error occurred on lss, error details; {exception}"
        )
        return JsonResponse({"error": error_message}, status=200)


def custom_exception_handler(exc, context):
    """Custom exception handler to return the error message in the response."""

    if settings.DEBUG:
        return rest_views.exception_handler(exc, context)

    original_exception = exc
    if isinstance(exc, Http404):
        exc = rest_exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = rest_exceptions.PermissionDenied()

    if not isinstance(exc, rest_exceptions.APIException):
        exc = rest_exceptions.APIException(
            detail={"error": str(exc) or "Unknown error"}
        )
        if exc.status_code >= 500:
            # If the exception is an error server keep default behavior
            return None

    headers = {}
    if hasattr(exc, "auth_header"):
        headers["WWW-Authenticate"] = exc.auth_header
    if hasattr(exc, "wait"):
        headers["Retry-After"] = "%d" % exc.wait

    data = (
        exc.detail if isinstance(exc.detail, (list, dict)) else {"detail": exc.detail}
    )
    rest_views.set_rollback()
    response = Response(data, status=exc.status_code, headers=headers)
    status_code = None

    if isinstance(response.data, dict):
        items_data = response.data.items()
        items_with_errors = {}
        for key, value in items_data:
            if key == "status_code":
                # Override status code if it is present in the data
                try:
                    if isinstance(value, (str, int)):
                        status_code = int(value)
                    elif isinstance(value, list) and value:
                        status_code = int(value[0])
                except ValueError:
                    pass
            elif isinstance(value, list):
                items_with_errors[key] = [msg for msg in value]
            elif isinstance(value, dict):
                if key in value.keys():
                    items_with_errors[key] = [str(value[key])]
                else:
                    items_with_errors[key] = [str(value)]
            else:
                items_with_errors[key] = [str(value)]
    else:
        items_with_errors = {"Invalid": [str(response.data[0])]}

    new_response = {
        "errors": [
            {"field": field.replace("_", " ").title(), "msgs": msgs}
            for field, msgs in items_with_errors.items()
        ],
        "status_code": status_code if status_code else response.status_code,
        "exception_type": original_exception.__class__.__name__,
    }

    response.data = new_response
    return response
