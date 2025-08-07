from rest_framework import serializers
from applications.parking.models import Reservation, Garages


class ReservationSerializer(serializers.ModelSerializer):
    garage = serializers.SlugRelatedField(queryset=Garages.objects.all(), slug_field='uuid')
    amount_payed = serializers.IntegerField(default=0, read_only=True)
    class Meta:
        model = Reservation
        fields = [
            "garage",
            "plate",
            "day",
            "start_time",
            "end_time",
            "amount_payed",
            "uuid"
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }


class DeleteReservationSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(default=0, write_only=True)
    class Meta:
        model = Reservation
        fields = [
            "amount",
            "uuid"
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }
