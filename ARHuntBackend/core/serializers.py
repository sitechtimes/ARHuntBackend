from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'score', 'grade']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user

class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = ['rat_type','scale','caught','score', 'user']
