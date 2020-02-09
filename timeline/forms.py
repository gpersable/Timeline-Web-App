from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']

class PostComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post_comment']