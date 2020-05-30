from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import OrderItem, CartItem
from .serializers import CartItemSerializer

# Create your views here.


class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user).select_related('menu_item').select_related('user')

    def create(self, request, *args, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
