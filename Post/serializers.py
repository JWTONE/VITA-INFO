from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
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
        ]
        read_only_fields = ["author", "category",]

    def get_like_users(self, obj):
        return obj.like_users.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('category', None)
        return representation

#    comments = CommentSerializer(many=True, read_only=True, required=False)
