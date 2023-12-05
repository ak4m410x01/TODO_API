from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save, post_delete

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_auth_token(sender, instance=None, **kwargs):
    Token.objects.filter(user=instance).delete()
