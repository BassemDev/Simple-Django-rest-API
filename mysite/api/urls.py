from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy, BlogPostList

urlpatterns = [
    path("blog-posts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blog-posts/<int:pk>/", BlogPostRetrieveUpdateDestroy.as_view(), name="update-delete-retrieve"),
    path("custom-blog-posts/", BlogPostList.as_view(), name="custom-get")
]