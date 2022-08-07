from dataclasses import field
from django import forms
from . models import Producto, CategoriaProd

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = '__all__'