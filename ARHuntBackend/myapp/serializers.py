from rest_framework import serializers
from .models import *

class RatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rats
        fields = '__all__'