from rest_framework import serializers

from applications.parking.models import HistoricalReservation


class HistoricalReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalReservation
        fields = ["garage", "plate", "day", "start_time", "end_time", "uuid", "amount_payed"]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }
