from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_backend.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a new post
    """
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner__username', 'owner__profile__id']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'owner__username']
    ordering_fields = ['like_count', 'comments_count', 'created_at',
                       'updated_at',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')