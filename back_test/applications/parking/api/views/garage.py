from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from applications.parking.models import Garages
from applications.parking.api.serializers.garage import GaragesSerializer


class GaragesViewSet(mixins.ListModelMixin, GenericViewSet):

    queryset = Garages.objects.all()
    serializer_class = GaragesSerializer
    http_method_names = ["get", ]
    lookup_field = "uuid"
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
