from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_backend.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsStaffOrReadOnly,]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()


class EventDelete(generics.DestroyAPIView):
    """
    Delete a event if you are staff.
    """
    serializer_class = EventSerializer
    permission_classes = [IsStaffOrReadOnly,]
    queryset = Event.objects.all()


class EventUpdate(generics.UpdateAPIView):
    """
    Update a event if you are staff.
    """
    serializer_class = EventSerializer
    permission_classes = [IsStaffOrReadOnly,]
    queryset = Event.objects.all()
