from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=150, default="Anon", unique=True)
    grade = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    score = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "grade"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Rat(models.Model):
    rat_type = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    caught = models.BooleanField(default=False)
    score = models.IntegerField(null=True)
    rarity = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qr_number = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
