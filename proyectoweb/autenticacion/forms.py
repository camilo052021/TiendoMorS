from django import forms
from . models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Password', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PefilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['usuario','ciudad', 'direccion', 'telefono']
        

# Para actualizar el perfil
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email',]

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['ciudad', 'direccion', 'telefono']