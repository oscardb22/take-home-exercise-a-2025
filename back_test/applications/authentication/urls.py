from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api.views.user import ProtectedView, UserViewSet

api_urls = routers.DefaultRouter(trailing_slash=True)
api_urls.register(r"users", UserViewSet, basename="user")


router_apirest = api_urls.urls

router_apirest += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected-view/', ProtectedView.as_view(), name='token_refresh'),
]
