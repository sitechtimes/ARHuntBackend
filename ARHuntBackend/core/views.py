from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView

class UserView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        return Response(UserSerializer(user, many=True).data)

class UserByName(APIView):
    def get(self, request, name):
        user = CustomUser.objects.get(name=name)
        return Response(UserSerializer(user).data)

class RegisterView(generics.CreateAPIView):
    users = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class RatView(APIView):
    def get(self, request):
        rats = Rat.objects.all()
        return Response(RatSerializer(rats, many=True).data)

    def post(self, request):
        
        serializer = RatSerializer(data=request.data,many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CatchRat(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        rat_id = request.data.get('rat_id')
        if not rat_id:
            return Response({"Error fetching rat"}, status=400)
        rat = get_object_or_404(Rat, rat_id = rat_id,user=user_id)
        if rat.caught:
            return Response({"This rat has been caught already."}, status=400)
        rat.caught = True
        rat.save()
        serializer = RatSerializer(rat)
        return Response(serializer.data, status=201)


