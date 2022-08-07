from pyexpat import model
from django import forms
from . models import Post, Categoria
from django.db.models import fields

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
