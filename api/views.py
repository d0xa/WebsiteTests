from .serializers import RoomSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all() #query set - what we want to return
    serializer_class = RoomSerializer # return format on how we want to see it