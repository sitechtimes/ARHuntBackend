from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from supa import supabase


class UserView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        return Response(UserSerializer(user, many=True).data)


class UserByName(APIView):
    def get(self, request, name):
        user = get_object_or_404(CustomUser, name=name)
        return Response(UserSerializer(user).data, status=201)


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


class CatchRat(APIView):
    def post(self, request):
        user_id = request.data.get("user")
        qr_number = request.data.get("qr_number")
        if not qr_number:
            return Response({"No qr number provided"}, status=400)
        rat = get_object_or_404(Rat, qr_number=qr_number, user=user_id)

        if rat.caught:
            return Response({"This rat has been caught already."}, status=400)
        rat.caught = True
        rat.save()
        serializer = RatSerializer(rat)
        return Response(serializer.data, status=201)


class ListAllFilesView(APIView):
    def get(self, request):
        bucket = "rat-models"

        files = supabase.storage.from_(bucket).list()
        all_files = []
        for file in files:
            file_path = f"{file['name']}"
            public_url = supabase.storage.from_(bucket).get_public_url(file_path)
            all_files.append(
                {
                    **file,
                    "url": public_url,
                }
            )

        return Response({"files": all_files})


class ListFileByTypeRarity(APIView):
    def get(self, request):
        bucket = "rat-models"
        file_path = f"{request.data['rat_type']}.glb"
        public_url = supabase.storage.from_(bucket).get_public_url(file_path)
        return Response({"url": public_url})
