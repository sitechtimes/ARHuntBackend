from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .serializers import *

class RatView(APIView):
    def get(self, request):
        rats = Rat.objects.all()
        return Response(RatSerializer(rats, many=True).data)

    def post(self, request):
        serializer = RatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



