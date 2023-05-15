from django.shortcuts import render
from profiles.models import Profile
from rest_framework import generics, permissions
from profiles.serializers import ProfileSerializer
from drf_api_backend.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileList(generics.ListCreateAPIView):
    """
    List all profiles or create a new profile by logging in.
    """
    queryset = Profile.objects.all().order_by("-created_at")
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile instance if you own it.
    """
    queryset = Profile.objects.all().order_by("-created_at")
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
