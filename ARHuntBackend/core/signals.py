from django.db.models.signals import post_save, pre_delete
from .models import *
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


@receiver(post_save, sender=Rat)
def update_score(sender, instance, created, **kwargs):
    if created:
        return

    try:
        previous = Rat.objects.get(pk=instance.pk)
    except Rat.DoesNotExist:
        return

    if instance.caught:
        user = previous.user
        user.score += instance.score
        user.save()
        previous.delete()
