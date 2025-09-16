from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListViewSet, CommentViewSet, VoteViewSet

router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"posts", PostListViewSet, basename="Post")
router.register(r"votes", VoteViewSet, basename="vote")

urlpatterns = router.urls

