from django import forms
from django.forms import ModelForm
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

