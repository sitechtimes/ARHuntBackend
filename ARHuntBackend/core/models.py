from django.db import models

# Create your models here.  

class Rat(models.Model):
    rat_type = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    caught = models.BooleanField(default = False)
    score = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)




