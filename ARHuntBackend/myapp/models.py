from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    score = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email

class User(models.Model):
    score = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)
    def __str__(self):
        return self.username


