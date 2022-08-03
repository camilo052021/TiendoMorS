from django.shortcuts import render
from .models import *
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    context = {'posts': posts, 'categorias':categorias}
    return render(request, "blog/blog.html", context)

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'posts':posts}
    return render(request, 'blog/categoria.html', context)

