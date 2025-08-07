from datetime import timedelta

REST_USE_JWT = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "uuid",
    "SLIDING_TOKEN_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

password_serializer = "applications.authentication.api.serializers."
reset_password_serializer = (
    f"{password_serializer}password_reset_serializer.PasswordResetConfirmSerializer"
)
password_serializer += "password_reset_serializer.PasswordResetSerializer"

login_serializer = "applications.authentication.api.serializers.login."
login_serializer += "PerformUserDetailsSerializer"

REST_AUTH_SERIALIZERS = {
    "PASSWORD_RESET_SERIALIZER": password_serializer,
    "PASSWORD_RESET_CONFIRM_SERIALIZER": reset_password_serializer,
    "USER_DETAILS_SERIALIZER": login_serializer,
}

REST_FRAMEWORK = {
    # Base API policies
    "DEFAULT_RENDERER_CLASSES": [
        "drf_orjson_renderer.renderers.ORJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework.renderers.AdminRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "drf_orjson_renderer.parsers.ORJSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    # Pagination
    "DEFAULT_PAGINATION_CLASS": "back_test.pagination.StandardResultsSetPagination",
    "PAGE_SIZE": 10,
    # Filtering
    "SEARCH_PARAM": "search",
    "ORDERING_PARAM": "order_by",
    # Versioning
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": "v1",
    "VERSION_PARAM": "version",
    # Input and output formats
    "DATE_FORMAT": "%Y/%m/%d",
    "DATE_INPUT_FORMATS": ["%Y/%m/%d"],
    "DATETIME_FORMAT": "%Y/%m/%d %H:%M:%S",
    "DATETIME_INPUT_FORMATS": ["%Y/%m/%d %H:%M:%S"],
    "TIME_FORMAT": "%H:%M:%S",
    "TIME_INPUT_FORMATS": ["%H:%M:%S"],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ],
    # "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
    # Custom error handlers
    "EXCEPTION_HANDLER": "back_test.general_error_handler.custom_exception_handler",
    "DEFAULT_THROTTLE_RATES": {
        "anon": "3/hour",
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
