from .models import Profile
from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
