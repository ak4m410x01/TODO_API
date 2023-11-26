from django.contrib import admin
from tasks.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "start_time",
        "end_time",
        "done",
        "created_at",
        "updated_at",
        "user",
    )
    list_filter = (
        "done",
        "user",
    )
    search_fields = (
        "title",
        "description",
    )
    ordering = ("start_time",)


admin.site.register(Task, TaskAdmin)
