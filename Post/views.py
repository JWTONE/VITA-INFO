from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from .models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer

def set_category(instance):
    if instance.is_staff:
        return "admin"
    else:
        return "review"


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    def post(self, request):  # 게시글 작성
        author = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author, category=set_category(author))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, post_pk):
        return get_object_or_404(Post, id=post_pk)

    def get(self, request, post_pk):
        post = self.get_object(post_pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
    def post(self, request, post_pk):
        post = self.get_object(post_pk)
        user = request.user
        if user in post.like_users.all():
            post.like_users.remove(user)
            post.like_counts -= 1
            post.save()
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            post.like_users.add(user)
            post.like_counts += 1
            post.save()
            return Response("좋아요 성공", status=status.HTTP_201_CREATED)
    
    def put(self, request, post_pk):
        post = self.get_object(post_pk)
        if post.author == request.user:
            serializer = PostDetailSerializer(
                post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, post_pk):
        post = self.get_object(post_pk)
        if post.author == request.user:
            post.delete()
            data = {"pk": f"{post_pk} is deleted."}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        ) | Post.objects.filter(
            author__nickname__icontains=query
        )
        serializer = PostSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request, post_pk, comment_pk=None):
        author = request.user
        post = get_object_or_404(Post, pk=post_pk)
        if comment_pk:
            comment = get_object_or_404(Comment, pk=comment_pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=author, post_id=post, is_reply=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=author, post_id=post, is_reply=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def put(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.author == request.user:
            serializer = CommentSerializer(
                comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)