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
        fields = ["qr_number", "rat_type", "scale", "caught", "score", "user", "name", "rarity"]
        
    def update(self, instance, validated_data):
        previous_caught = instance.caught

        instance = super().update(instance, validated_data)

        if not previous_caught and instance.caught:
            user = instance.user
            user.score += instance.score  
            user.save()
            instance.delete()

        return instance
