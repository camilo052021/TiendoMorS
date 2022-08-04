from django.core.paginator import Paginator
from django.shortcuts import render
from django.http.response import Http404
from .models import CategoriaProd, Producto
#from carro.context_processor import *

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()
    paginador = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginador.get_page(page_number)
    context  ={'productos': productos, 'categorias': categorias,'productos':page_obj}
    return render(request, "tienda/tienda.html",context)

def categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    context  ={'productos': productos, 'categoria': categoria}
    return render(request, 'tienda/categoria.html', context) 