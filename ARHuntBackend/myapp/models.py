from django.db import models

class User(models.Model):
    score = models.IntegerField(default=0)
    email = models.EmailField(unique=True, help_text="Enter a valid email address.")
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)
    def __str__(self):
        return self.username


