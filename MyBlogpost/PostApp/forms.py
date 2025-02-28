from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    parent_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Hidden field for replies

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
