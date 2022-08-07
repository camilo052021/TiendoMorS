from dataclasses import field
from django import forms
from . models import Producto, CategoriaProd

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
