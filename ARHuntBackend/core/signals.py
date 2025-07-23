from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import Rat
from django.dispatch import receiver

@receiver(post_save, sender=Rat) 
def update_score(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
 
