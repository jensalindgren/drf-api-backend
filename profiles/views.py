from django.shortcuts import render
from profiles.models import Profile
from rest_framework import generics, filters
from profiles.serializers import ProfileSerializer
from drf_api_backend.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListCreateAPIView):
    """
    List all profiles or create a new profile by logging in.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile instance if you own it.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
