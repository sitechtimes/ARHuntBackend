from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    grade = models.IntegerField(default=0)
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'grade']

    objects = CustomUserManager()
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email




