from django.shortcuts import render
from .models import *
#from carro.context_processor import *

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, "tienda/tienda.html",context)