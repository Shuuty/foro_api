from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-create_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
