from django.db.models.signals import pre_save, pre_delete
from .models import *
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

@receiver(pre_save, sender=Rat) 
def update_score(sender, instance, **kwargs):
    if instance.id is None:
        return
    previous = Rat.objects.get(rat_id=instance.rat_id)

    if instance.id is not None and not previous.caught:
        user = get_object_or_404(CustomUser,pk = instance.user_id)
        user.score+=instance.score
        user.save()
        return Response({"you did it!"},status=400)
        
 
