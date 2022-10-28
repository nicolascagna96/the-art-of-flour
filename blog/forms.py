from django import forms
from django.forms import ModelForm
from .models import Comment
from .models import Recipes
from .models import Contact
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Create Submit Recipes Form


class SubmitForm(ModelForm):

    class Meta:
        model = Recipes
        fields = (
            'name', 'email', 'recipe_name', 'body', 'image')

        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'recipe_name': 'Recipe Title',
            'body': 'Ingredients and Method',
        }

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form:control'}),
            'email': forms.EmailInput(attrs={'class': 'form:control'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form:control'}),
            'body': forms.TextInput(attrs={'class': 'form:control'}),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'body': 'Message',
        }
