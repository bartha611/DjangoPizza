from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuItem, Topping
from .serializers import MenuItemSerializer, ToppingSerializer

# Create your views here.


class MenuView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ToppingView(ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
