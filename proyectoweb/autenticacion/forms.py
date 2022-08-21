from django import forms
from . models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PefilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['ciudad', 'direccion', 'telefono']
        
        