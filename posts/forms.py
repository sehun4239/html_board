# forms.py

from django import forms
from posts.models import Post, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['contents', 'texts']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply']

