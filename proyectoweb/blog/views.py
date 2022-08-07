from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    context = {'posts': posts, 'categorias': categorias}
    return render(request, "blog/blog.html", context)

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    context={'categoria':categoria,"posts": posts }
    return render(request, "blog/categoria.html", context)

@login_required
def agregar_post(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog:blog')
        else:
            form = PostForm()

        context = {'form':form}
        return render(request, 'blog/agregar_post.html', context)

@login_required
def editar_post(request, id):
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=id)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('blog:blog')
        else:
            form = PostForm(instance=post)
        
        context = {'form':form}
        return render(request,'blog/editar_post.html', context)

@login_required
def eliminar_post(request, id):
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('blog:blog')
