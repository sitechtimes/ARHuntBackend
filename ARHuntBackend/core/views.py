from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
class UserView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        return Response(UserSerializer(user, many=True).data)

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

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



