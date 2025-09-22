from rest_framework import permissions, viewsets
from .permissions import IsAuthorOrReadOnly, IsAuthorOrCommunityOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, VoteSerializer, CommunitySerializer
from .models import Post, Comment, Vote, Community
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all ()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    #Filtros de busqueda
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['community', 'author']
    search_fieds = ["title", "content"]
    ordering_fields = ["create_at", "title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,  IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.data.get("post")
        post = Post.objects.get(id=post_id)
        value = self.request.data.get("value")

        vote, created = Vote.objects.update_or_create(
            user=self.request.user,
            post=post,
            defaults={"value": value}
        )
        serializer.instance = vote
    
    @action(detail=False, methods=["get"])
    def my_votes(self, request):
        votes = Vote.objects.filter(user=request.user)
        serializer= self.get_serializer(votes, many=True)
        return Response(serializer.data)
    
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrCommunityOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

