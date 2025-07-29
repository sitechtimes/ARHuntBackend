from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "name", "score", "grade", "password"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = ["rat_id", "rat_type", "scale", "caught", "score", "user"]
