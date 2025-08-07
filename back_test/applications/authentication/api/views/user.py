from django_filters import rest_framework as filters
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from applications.authentication.api.helpers.user import UserDB
from applications.authentication.api.serializers.user import (
    SetNewPasswordSerializer,
    UserSerializer,
)
from applications.authentication.models import User


class UserFilter(filters.FilterSet):
    """docstring for GroupFilter"""

    group = filters.CharFilter(
        field_name="groups__name", lookup_expr="icontains", label="group"
    )
    trainer = filters.BooleanFilter(method="query_trainer", label="trainer")

    class Meta:
        model = User
        fields = ["uuid"]

    order_by = filters.OrderingFilter(
        fields=(("first_name", "name"),),
        label="order by",
    )


class UserViewSet(
    mixins.UpdateModelMixin, mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, mixins.ListModelMixin,
    GenericViewSet):
    """
    docstring for UserViewSet
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "patch"]
    lookup_field = "uuid"
    parser_classes = (MultiPartParser, FormParser)
    # filterset_class = UserFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.exclude(email="oscar@oscar.com")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        """docstring for get_queryset"""
        queryset = super().get_queryset()
        if self.action == "set_new_password":
            queryset = queryset.filter(uuid=self.request.user.uuid)
        return queryset

    @action(methods=["post"], detail=False, url_path="set-new-password")
    def set_new_password(self, request, *args, **kwargs):
        """docstring for bulk_actions"""
        context = self.get_serializer_context()
        serializer = SetNewPasswordSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        UserDB(
            user=self.request.user,
            password=request.data.get("new_password"),
        ).set_new_password()
        return Response(status=status.HTTP_200_OK)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        response = {"status": " hey Im here"}
        return Response(response)
