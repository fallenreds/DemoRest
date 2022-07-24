from django.shortcuts import render
from rest_framework import generics
# Create your views here.


class CarCreateView(generics.CreateAPIView):
    serializer_class = ...
