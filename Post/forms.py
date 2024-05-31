from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["author", "like_users", "like_counts", "category"]
        labels = {
            "title" : "제목",
            "content" : "내용",
            "image" : "이미지"
        }