from rest_framework import serializers

from applications.parking.models import Garages


class GaragesSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer"""

    class Meta:
        model = Garages
        fields = [
            "name",
            "uuid",
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }
