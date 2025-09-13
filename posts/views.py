from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-create_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
