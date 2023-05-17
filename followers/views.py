from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api_backend.permissions import IsOwnerOrReadOnly
from .models import Follower, FollowerEvents
from .serializers import FollowerSerializer
from .serializers import FollowerEventsSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List followers or create a follower if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):

    permisson_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowedEventsList(generics.ListAPIView):
    """
    List events that are followed by the logged in user.
    """
    queryset = FollowerEvents.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerEventsSerializer

    def get_queryset(self):
        user = self.request.user
        return Follower.objects.filter(owner=user)


class FollowerEventsDetail(generics.RetrieveDestroyAPIView):

    permisson_classes = [IsOwnerOrReadOnly]
    queryset = FollowerEvents.objects.all()
    serializer_class = FollowerEventsSerializer
