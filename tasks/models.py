from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from rest_framework.authtoken.models import Token

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_auth_token(sender, instance=None, **kwargs):
    Token.objects.filter(user=instance).delete()
