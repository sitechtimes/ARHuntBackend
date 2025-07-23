from django.contrib.auth.models import Group, User
from rest_framework import serializers

from users.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'score', 'grade']