from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "start_time",
            "end_time",
            "done",
            "created_at",
            "updated_at",
            "user",
        )
        extra_kwargs = {
            "user": {
                "read_only": True,
                "required": False,
            },
        }
        ordering = ("id",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "auth_token",
            "email",
            "first_name",
            "last_name",
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
            },
        }
        ordering = ("id",)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.password = make_password(validated_data["password"])
        instance.save()
        return instance
