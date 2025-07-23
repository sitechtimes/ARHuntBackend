from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    grade = models.IntegerField(default=0, null=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email

class Rat(models.Model):
    rat_type = models.CharField()
    scale = models.CharField()
    caught = models.BooleanField(default = False)
    score = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


