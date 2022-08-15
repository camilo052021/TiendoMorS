from pyexpat import model
from tkinter.tix import Form
from django import forms
from . models import Pedido, LineaPedido
from django.db.models import fields

class LineaPedidoForm(forms.ModelForm):
    class Meta:
        model = LineaPedido
        fields = '__all__'