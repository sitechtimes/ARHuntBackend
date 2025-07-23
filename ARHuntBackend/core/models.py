from django.db import models

# Create your models here.  

class Rat(models.Model):
    rat_type = models.CharField()
    scale = models.CharField()
    caught = models.BooleanField(default = False)
    score = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)




