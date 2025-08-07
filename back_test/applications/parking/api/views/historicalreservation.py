from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from applications.parking.models import HistoricalReservation, Reservation
from applications.parking.api.serializers.historicalreservation import HistoricalReservationSerializer
from applications.parking.api.serializers.reservation import ReservationSerializer


class HistoricalReservationViewSet(mixins.ListModelMixin, GenericViewSet):

    queryset = HistoricalReservation.objects.all()
    serializer_class = HistoricalReservationSerializer
    http_method_names = ["get", ]
    lookup_field = "uuid"
    permission_classes = []

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="plate",
                type=str,
                description="received a plate.",
                required=True,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        plate = request.query_params.get("plate")
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(plate=plate)
        serializer = self.get_serializer(queryset, many=True)
        queryset_reservation = Reservation.objects.filter(plate=plate)
        reservation_serializer = ReservationSerializer(queryset_reservation, many=True)
        return Response(serializer.data + reservation_serializer.data)
