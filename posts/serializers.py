from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', "author_username", "create_at"]
        read_only_fields = ['id', 'author', 'create_at']