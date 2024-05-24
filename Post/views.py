from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request):  # 게시글 작성
        author = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)