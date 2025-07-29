from django.db.models.signals import post_save, pre_delete
from .models import *
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


@receiver(post_save, sender=Rat)
def update_score(sender, created, instance, **kwargs):
    previous = Rat.objects.get(rat_id=instance.rat_id)

    if not previous.caught and not created:
        user = get_object_or_404(CustomUser, pk=instance.user_id)
        user.score += instance.score
        user.save()
        return Response({"you did it!"}, status=400)
