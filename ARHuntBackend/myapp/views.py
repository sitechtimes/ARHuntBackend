from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView,Response

# Create your views here.
class RatsView(APIView):
    def get(self, request):
        rats = Rats.objects.all()
        serializer = RatsSerializer(rats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)