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
    users = CustomUser.objects.all()
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

from supa import supabase

class ListAllFilesView(APIView):
    def get(self, request):
        bucket = "rat-models"

        files = supabase.storage.from_(bucket).list()
        all_files = []
        for file in files:
            file_path = f"{file['name']}"
            public_url = supabase.storage.from_(bucket).get_public_url(file_path)
            all_files.append({
                **file,
                "url": public_url,
            })
        
        return Response({"files": all_files})

class ListFileByTypeRarity(APIView):
    def get(self, request):
        bucket = "rat-models"
        file_path = f"{request.data['rat_type']}.glb"
        public_url = supabase.storage.from_(bucket).get_public_url(file_path)
        return Response({"url": public_url})
