from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["author", "like_users", "like_counts", "category", "image"]
        labels = {
            "title": "제목",
            "content": "내용",
        }
        widgets = {
            'content': forms.CharField(widget=CKEditorUploadingWidget())
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
