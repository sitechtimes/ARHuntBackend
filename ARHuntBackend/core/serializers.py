from rest_framework import serializers
from .models import *

class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = ['rat_type','scale','caught','score']