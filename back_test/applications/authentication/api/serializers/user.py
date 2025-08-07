from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from applications.authentication.models import User


class UserSerializerBase(serializers.ModelSerializer):
    """docstring for UserSerializer"""

    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }


class UserSerializer(UserSerializerBase):
    """docstring for UserSerializer"""

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    picture_profile = serializers.ImageField(
        allow_null=True, allow_empty_file=True, required=False)
    file_info = serializers.FileField(
        allow_null=True, allow_empty_file=True, required=False)

    class Meta:
        model = User
        fields = ["groups", "picture_profile", "file_info"] + UserSerializerBase.Meta.fields
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
        }


class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    new_password2 = serializers.CharField(required=False)
    old_password = serializers.CharField(required=False)

    def validate(self, attrs):
        super().validate(attrs)
        old_password = attrs.pop("old_password", None)
        new_password = attrs.pop("new_password", None)
        new_password2 = attrs.pop("new_password2", None)
        user = self.context["request"].user
        if old_password and not user.check_password(old_password):
            raise serializers.ValidationError("Wrong current password")
        elif user.has_usable_password() and user.password != "":
            raise serializers.ValidationError("previous password not provided")
        elif new_password2 != new_password:
            raise serializers.ValidationError("both password have to match")
        validate_password(new_password)
        return attrs
