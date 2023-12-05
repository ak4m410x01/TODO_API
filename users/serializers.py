from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer, StringRelatedField


class UserSerializer(ModelSerializer):
    tasks = StringRelatedField(many=True, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "auth_token",
            "first_name",
            "last_name",
            "email",
            "last_login",
            "date_joined",
            "tasks",
        )
        extra_kwargs = {
            "auth_token": {
                "read_only": True,
                "required": False,
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "tasks": {
                "read_only": True,
                "required": False,
            },
        }
        ordering = ("id",)

    # hash password & create token on create new user before save in db
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User(**validated_data)
        user.save()

        return user

    # hash password on update user password before save in db
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.password = make_password(validated_data["password"])
        instance.save()
        return instance
