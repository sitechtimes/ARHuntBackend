from django.db import models

# Create your models here.

class Rats(models.Model):
    rat_type = models.CharField()
    scale = models.CharField()
    caught = models.BooleanField(default = False)
    score = models.IntegerField()
    rat_id = models.IntegerField()
    user_id = models.IntegerField()



