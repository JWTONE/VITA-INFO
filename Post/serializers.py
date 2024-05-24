from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
#    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "content",
            "image",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author",]
        
class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "content",
            "image",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author",]
        
#    comments = CommentSerializer(many=True, read_only=True, required=False)