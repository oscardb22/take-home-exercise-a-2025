from django.urls import path
from rest_framework import routers
from .api.views.garage import GaragesViewSet
from .api.views.reservation import ReservationApiView, ReservationViewSet
from .api.views.historicalreservation import HistoricalReservationViewSet

api_urls = routers.DefaultRouter(trailing_slash=True)
api_urls.register(r"garage", GaragesViewSet, basename="garage")
api_urls.register(r"historical", HistoricalReservationViewSet, basename="historical")
api_urls.register(r"payment", ReservationViewSet, basename="payment")


router_apirest = api_urls.urls

router_apirest += [
    path('free_spots/', ReservationApiView.as_view(), name='reservation_list'),
]
