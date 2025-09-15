from rest_framework import serializers
from .models import Post, Comment

    
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username",read_only=True)

    class Meta:
        model = Comment
        fields = ['id','content', 'author', 'post', "created_at"]
        read_only_fields = ['author', "created_at"]

class PostSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True, read_only=True)
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', "author_username", "create_at", "comments"]
        read_only_fields = ['id', 'author', 'create_at']