from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView,Response

# Create your views here.
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
    def post(self,request):
        caught_rat = Rat.objects.get(id = request.id)
        



