from collections import defaultdict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django_redis import get_redis_connection
from .models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

##################
#       API      #
##################


def set_category(instance):
    if instance.is_staff:
        return "info"
    else:
        return "review"


class PostListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category = self.kwargs.get('category')  # URL 파라미터에서 category 가져오기
        if category:
            # category로 필터링된 게시글 반환
            return Post.objects.filter(category=category).order_by('-id')
        return Post.objects.all().order_by('-id')

    def post(self, request):  # 게시글 작성
        author = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author, category=set_category(author))
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk):
        return get_object_or_404(Post, id=post_pk)

    def get(self, request, post_pk):
        post = self.get_object(post_pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def post(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk)
            user = request.user
            if user in post.like_users.all():
                post.like_users.remove(user)
                post.like_counts -= 1
            else:
                post.like_users.add(user)
                post.like_counts += 1
            post.save()

            # 응답 데이터에 like_counts 포함하여 반환
            serializer = PostSerializer(post)  # 포스트 모델에 맞는 직렬화된 데이터를 사용
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

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
        if post.author == request.user or request.user.is_staff:
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

        if results:
            redis_conn = get_redis_connection("default")
            redis_conn.zincrby('search_keywords', 1, query)

        # 카테고리별로 결과를 그룹화
        categorized_results = defaultdict(list)
        for post in results:
            categorized_results[post.category].append(post)

        # 결과를 직렬화
        serialized_results = {}
        for category, posts in categorized_results.items():
            serialized_results[category] = PostSerializer(
                posts, many=True).data

        return Response(serialized_results, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# 실시간 검색어 순위


@api_view(['GET'])
def ranking(request):
    redis_conn = get_redis_connection("default")
    # 상위 10개의 인기 검색어를 가져옴
    popular_keywords = redis_conn.zrevrange(
        'search_keywords', 0, 9, withscores=True)

    # 순위 매기기
    ranked_keywords = []
    for index, (keyword, count) in enumerate(popular_keywords, start=1):
        ranked_keywords.append({
            'rank': index,
            'keyword': keyword.decode('utf-8'),
            'count': int(count)
        })

    return Response(ranked_keywords, status=status.HTTP_200_OK)


class CommentListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # 중복된 답글을 저장할 집합
        duplicate_replies = set()

        # replies를 각 부모 댓글에 추가하고 중복된 답글을 찾아냄
        for comment in data:
            if comment['is_reply']:
                parent_comment_id = comment['comment_id']
                if parent_comment_id in duplicate_replies:
                    # 중복된 답글이면 삭제
                    data.remove(comment)
                else:
                    # 중복된 답글이 아니면 집합에 추가
                    duplicate_replies.add(parent_comment_id)

        return Response(data)

    def post(self, request, post_pk, comment_pk=None):
        author = request.user
        post = get_object_or_404(Post, pk=post_pk)
        if comment_pk:
            comment = get_object_or_404(Comment, pk=comment_pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=author, comment_id=comment,
                                post_id=post, is_reply=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=author, post_id=post, is_reply=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, id=comment_pk)

    def post(self, request, comment_pk):
        try:
            comment = self.get_object(comment_pk)
            user = request.user
            if user in comment.like_comments.all():
                comment.like_comments.remove(user)
                comment.like_counts -= 1
            else:
                comment.like_comments.add(user)
                comment.like_counts += 1
            comment.save()

            # 응답 데이터에 like_counts 포함하여 반환
            serializer = CommentSerializer(comment)  # 포스트 모델에 맞는 직렬화된 데이터를 사용
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        if comment.author == request.user:
            serializer = CommentSerializer(
                comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        if comment.author == request.user:
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
