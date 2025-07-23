from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'score', 'grade']

class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = ['rat_type','scale','caught','score', 'user']
