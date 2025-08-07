from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationTypeAdmin(admin.ModelAdmin):
    search_fields = ("app_label",)
