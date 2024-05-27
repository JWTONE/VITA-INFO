from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path("", views.PostListAPIView.as_view(), name="post_list"),
     path("<int:post_pk>/", views.PostDetailAPIView.as_view(),name="post_detail"),
     path("<int:post_pk>/comment/", views.CommentListAPIView.as_view(),name="post_comment"),
     path("<int:post_pk>/comment/<int:comment_pk>/", views.CommentListAPIView.as_view(),name="post_comment_reply"),
     path("comment/<int:comment_pk>/", views.CommentListAPIView.as_view(),name="post_comment_reply"),
     path("search/", views.search, name="search"),
]