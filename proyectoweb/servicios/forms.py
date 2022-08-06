from django import forms
from . models import Servicio
from django.db.models import fields

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

    widgets = {
        'titulo': forms.TextInput(attrs={'class':'from-control mt2', 'palceholder':'Titulo'}),
        'contenido': forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Contenido'}),
        'image': forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
    }