from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListCreateView, CommentViewSet

router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path('', PostListCreateView.as_view(), name="post-list-create"),
    path('', include(router.urls))
]
