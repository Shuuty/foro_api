from rest_framework import serializers
from .models import Post, Comment, Vote


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username",read_only=True)

    class Meta:
        model = Comment
        fields = ['id','content', 'author', 'post', "created_at"]
        read_only_fields = ['author', "created_at"]

class PostSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True, read_only=True)
    score = serializers.SerializerMethodField()
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', "author_username", "create_at", 'score' , "comments"]
        read_only_fields = ['id', 'author', 'create_at']

    def get_score(self, obj):
        return sum(v.value for v in obj.votes.all())

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Vote
        fields = ['id', 'user', 'post', 'value']
        read_only_fields = ['user']
