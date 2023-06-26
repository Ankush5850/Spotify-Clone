from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from rest_framework import generics
from .models import Room

from .serializers import Roomserializers
# Create your views here.
# def home(request):
#     print("ankush")
#     return HttpResponse("Home")

class RoomView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class = Roomserializers


