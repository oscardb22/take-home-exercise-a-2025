from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from datetime import datetime, timedelta
from applications.parking.models import Garages, Reservation, HistoricalReservation
from applications.parking.api.serializers.reservation import ReservationSerializer, DeleteReservationSerializer


class ReservationApiView(APIView):
    http_method_names = ["get", "post"]
    lookup_field = "uuid"
    permission_classes = []
    serializer_class = ReservationSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="garage_id",
                type=str,
                description="received a garage_id.",
                required=True,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        garage = Garages.objects.get(uuid=request.query_params.get('garage_id'))
        schedule = []
        current_time = datetime.now().replace(minute=0, second=0, microsecond=0)
        end_time = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
        count = 0
        while current_time <= end_time:
            next_time = current_time + timedelta(hours=1)
            reservation =  Reservation.objects.filter(
                garage=garage,
                day=current_time.date(),
                start_time=current_time.time(),
                end_time=next_time.time()
            ).only("uuid").exists()
            if not reservation:
                schedule.append(
                    {
                        "name": garage.name,
                        "garage": garage.uuid,
                        "day": current_time.strftime("%Y/%m/%d"),
                        "start_time": current_time.time(),
                        "end_time": next_time.time(),
                        "count": count
                    }
                )
            current_time = next_time
            count += 1
        response = {
            "count": len(schedule),
            "next": None,
            "previous": None,
            "results": schedule
        }
        return Response(response, status=status.HTTP_200_OK)

    @extend_schema(
        request=ReservationSerializer,
        responses={201: ReservationSerializer},
        examples=[
            OpenApiExample(
                "Example Request Body",
                value={
                    "garage": "85fdd9f1-fd42-4913-860f-eb51cedd5ae1",
                    "day": "2025/08/06",
                    "start_time": "20:00:00",
                    "end_time": "21:00:00",
                    "plate": "NQZ777"
                },
                request_only=True,
                media_type="application/json",
            ),
            OpenApiExample(
                "Example Successful Response",
                value={
                    "garage": "85fdd9f1-fd42-4913-860f-eb51cedd5ae1",
                    "day": "2025/08/06",
                    "start_time": "20:00:00",
                    "end_time": "21:00:00",
                    "plate": "NQZ777"
                },
                response_only=True,
                media_type="application/json",
                status_codes=["201"],
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @staticmethod
    def get_success_headers(data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ReservationViewSet(mixins.DestroyModelMixin, GenericViewSet):

    queryset = Reservation.objects.all()
    http_method_names = ["delete", ]
    serializer_class = DeleteReservationSerializer
    lookup_field = "uuid"
    permission_classes = []

    @extend_schema(
        request=DeleteReservationSerializer,
        responses={204: DeleteReservationSerializer},
        examples=[
            OpenApiExample(
                "Example Request Body",
                value={
                    "uuid": "85fdd9f1-fd42-4913-860f-eb51cedd5ae1",
                    "amount": 5000,
                },
                request_only=True,
                media_type="application/json",
            ),
            OpenApiExample(
                "Example Successful Response",
                value={
                    "transactional_id": "85fdd9f1-fd42-4913-860f-eb51cedd5ae1",
                },
                response_only=True,
                media_type="application/json",
                status_codes=["204"],
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        transactional_id = instance.make_payment(request.data.get("plate", 10), None)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={"transactional_id": transactional_id})
