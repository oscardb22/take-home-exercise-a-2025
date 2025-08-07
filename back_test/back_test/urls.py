"""
URL configuration for back_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from applications.authentication.urls import api_urls as api_urls_authentication

from applications.parking.urls import api_urls as api_urls_parking

urls_api = [
    path(
        "authentication/",
        include(
            (api_urls_authentication.urls, "authentication"),
            namespace="authentication",
        ),
    ),
    path(
        "parking/",
        include(
            (api_urls_parking.urls, "parking"),
            namespace="parking",
        ),
    ),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"),
    re_path(r"^api/", include(urls_api)),
]
