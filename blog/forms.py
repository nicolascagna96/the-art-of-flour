from django import forms
from django.forms import ModelForm
from .models import Comment
from .models import Recipes
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SubmitForm(ModelForm):
    user_name = forms.TextInput()
    recipe_name = forms.TextInput()
    body = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = Recipes
        fields = '__all__'