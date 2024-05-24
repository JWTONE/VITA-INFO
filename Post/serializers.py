from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "username",
            "content",
            "created_at",
            "updated_at",
            "like_count",
        ]

    def get_like_count(self, obj):
        return obj.like.count()