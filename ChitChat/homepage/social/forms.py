from django import forms 
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label = '',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Tell us how you did it:'

        })
    )
    art = forms.ImageField(
        label=''
    )

    class Meta:
        model = Post 
        fields = ['body', 'art']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label = '',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Comment...'

        })
    )

    class Meta:
        model = Comment
        fields = ['comment']