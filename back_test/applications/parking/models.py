from applications.authentication.models import CommonInfo, models
from django.utils.translation import gettext_lazy as _
# from django.utils import timezone


class Garages(CommonInfo):
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Name for the garage."),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this garage should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = "parking"
        db_table = "parking_garages"
        ordering = ["name"]
        verbose_name = _("garage")
        verbose_name_plural = _("garages")


class Reservation(CommonInfo):
    garage = models.ForeignKey(
        related_name="reservations",
        related_query_name="reservation",
        on_delete=models.CASCADE,
        to=Garages,
    )
    plate = models.CharField(
        verbose_name=_("Plate"),
        help_text=_("Car's Plate.")
    )
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this garage should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def __str__(self):
        return f"{self.garage} {self.plate} {self.day} {self.start_time} {self.end_time}"

    def make_payment(self, amount, customer_id):
        return HistoricalReservation.objects.create(
            garage=self.garage,
            plate=self.plate,
            day=self.day,
            start_time=self.start_time,
            end_time=self.end_time,
            amount_payed=amount
        ).uuid

    class Meta:
        unique_together = [["garage", "plate", "day", "start_time", "end_time"]]
        app_label = "parking"
        db_table = "parking_reservation"
        ordering = ["plate"]
        verbose_name = _("reservation")
        verbose_name_plural = _("reservations")


class HistoricalReservation(CommonInfo):
    garage = models.ForeignKey(
        related_name="historicalreservations",
        related_query_name="historicalreservation",
        on_delete=models.CASCADE,
        to=Garages,
    )
    plate = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Name for the garage.")
    )
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    amount_payed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.plate

    class Meta:
        app_label = "parking"
        db_table = "parking_historical_reservation"
        ordering = ["plate"]
        verbose_name = _("historical_reservation")
        verbose_name_plural = _("historical_reservations")
