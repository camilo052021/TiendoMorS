from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoriaProd, Producto
from django.contrib.auth.decorators import login_required
from . forms import CategoriaProductoForm, ProductoForm
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

def categorias_producto(request):
    categorias_producto = CategoriaProd.objects.all()
    context = {'categorias_producto': categorias_producto}
    return render(request, 'categoria_producto/categorias_p.html', context)

@login_required
def agregar_categoria_p(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CategoriaProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('tienda')
        else:
            form = CategoriaProductoForm()

        context = {'form':form}
        return render(request, 'categoria_producto/agregar_categoria_p.html', context)

@login_required
def editar_categoria_p(request, id):
    if request.user.is_superuser:
        categoria_prod = get_object_or_404(CategoriaProd, pk=id)
        if request.method == 'POST':
            form = CategoriaProductoForm(request.POST, instance=categoria_prod)
            if form.is_valid():
                form.save()
                return redirect('tienda')
        else:
            form = CategoriaProductoForm(instance=categoria_prod)
        
        context = {'form':form}
        return render(request, 'categoria_producto/editar_categoria_p.html', context)

@login_required
def eliminar_categoria_p(request, id):
    if request.user.is_superuser:
        categoria_prod = get_object_or_404(CategoriaProd, pk=id)
        categoria_prod.delete()
        return redirect('tienda')

@login_required
def agregar_producto(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('tienda')
        else:
            form = ProductoForm()

        context = {'form':form}
        return render(request, 'productos/agregar_producto.html', context)

@login_required
def editar_producto(request, id):
    if request.user.is_superuser:
        producto = get_object_or_404(Producto, pk=id)
        if request.method == 'POST':
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('tienda')
        else:
            form = ProductoForm(instance=producto)
        
        context = {'form':form}
        return render(request, 'productos/editar_producto.html', context)

@login_required
def eliminar_producto(request, id):
    if request.user.is_superuser:
        producto = get_object_or_404(Producto, pk=id)
        producto.delete()
        return redirect('tienda')