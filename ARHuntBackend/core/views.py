from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

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

        

class InitRats(APIView):
    def post(self,request):
        serializer = RatSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CatchRat(APIView):
    def post(self,request):
        user_id = request.user
        rat_id = request.data.get('id')
        if not rat_id:
            return Response({"error fetching rat"}, status=400)
        rat = get_object_or_404(Rat,pk = rat_id)
        if rat.caught:
            return Response({"this rat has been caught already"}, status=400)
        rat.caught = True
        rat.save()
        serializer = RatSerializer(rat)
        return Response(serializer.data, status=201)


