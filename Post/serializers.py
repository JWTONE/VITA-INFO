from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment_id',
            "content", 
            "author",
            "created_at",
            "is_reply",
            "replies",
        ]
        read_only_fields = ["author", "is_reply","id", "comment_id"]

    def get_replies(self, obj):
        replies = Comment.objects.filter(comment_id=obj.id)
        return CommentSerializer(replies, many=True).data if replies.exists() else None
    
        
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",   
            "title",
            "content",
            "image",
            "author",
            "category",
            "like_counts",
        ]
        read_only_fields = ["author", "category",]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('content', None)
        return representation

class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "author",
            "category",
            "like_counts",
            "created_at",
            "updated_at",
            "comments"
        ]
        read_only_fields = ["author", "category",]

    def get_comments(self, instance):
        comments = Comment.objects.filter(comment_id__isnull=True, post_id=instance.id)
        return CommentSerializer(comments, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('category', None)
        return representation



