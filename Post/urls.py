from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path("", views.PostListAPIView.as_view(), name="post_list"),
     path("<int:post_pk>/", views.PostDetailAPIView.as_view(),name="post_detail"),
]