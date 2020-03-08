from django import forms
from .models import Post,Comment,SubComment

class CreatePostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Yellow; border-radius: 8px; border-width: large;',
    }))
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':13,"cols":80}))
    class Meta:
        model=Post
        fields=['title','content',]


class CommentPostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Grey; border-radius: 8px; border-width: large;',
    }))
    class Meta:
        model=Comment
        fields=['content',]


class SubCommentPostForm(forms.ModelForm):
    content=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border:1px solid Grey; border-radius: 8px; border-width: large;',
    }))
    class Meta:
        model=SubComment
        fields=['content',]



