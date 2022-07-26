from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Car
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)