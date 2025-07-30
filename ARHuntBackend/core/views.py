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

class ListFoldersView(APIView):
    def get(self, request):
        bucket = request.query_params.get("bucket")
        if not bucket:
            return Response({"error": "Missing bucket parameter"}, status=400)

        folders = request.query_params.getlist("folder")
        if not folders:
            return Response({"error": "At least one folder param is required"}, status=400)
        
        response_data = {}
        for folder in folders:
            files = supabase.storage.from_(bucket).list(folder)
            folder_files = []
            for file in files:
                file_path = f"{folder}/{file['name']}"
                public_url = supabase.storage.from_(bucket).get_public_url(file_path)
                folder_files.append({
                    **file,
                    "url": public_url,
                })
            response_data[folder] = folder_files

        return Response({"files": response_data})