from rest_framework.serializers import ModelSerializer, StringRelatedField
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    user = StringRelatedField(required=False)
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


