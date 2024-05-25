from django import forms
from blog.models import Author, Category, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
