from django.contrib import admin
from .models import Reservation, HistoricalReservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    search_fields = ("app_label",)


@admin.register(HistoricalReservation)
class HistoricalReservationAdmin(admin.ModelAdmin):
    search_fields = ("app_label",)
