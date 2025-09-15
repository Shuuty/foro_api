from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"posts", PostListViewSet, basename="Post")

urlpatterns = router.urls

