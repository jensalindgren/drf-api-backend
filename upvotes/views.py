from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api_backend.permissions import IsOwnerOrReadOnly
from upvotes.models import UpVote
from upvotes.serializers import UpVoteSerializer


class UpVoteList(generics.ListCreateAPIView):
    """
    List all upvote or create a new upvote.
    """
    queryset = UpVote.objects.all()
    serializer_class = UpVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an upvote instance.
    """
    queryset = UpVote.objects.all()
    serializer_class = UpVoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
