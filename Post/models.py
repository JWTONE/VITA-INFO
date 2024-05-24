from django.db import models
from Account.models import User
from django.conf import settings

def get_image_upload_path(instance, filename):
    if instance.author.is_staff: 
        return f"admins/{filename}"
    elif instance.author.is_authenticated:
        return f"reviews/{filename}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=get_image_upload_path)
    category = models.CharField(max_length=30)
    author = models.ForeignKey(User, to_field="nickname", on_delete=models.CASCADE, related_name="post")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, to_field="nickname", on_delete=models.CASCADE, related_name="comment_author")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_likes = models.ManyToManyField(User,related_name="comment_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #대댓글
    is_reply = models.BooleanField()
    depth = models.IntegerField(null=True, blank=True)
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
