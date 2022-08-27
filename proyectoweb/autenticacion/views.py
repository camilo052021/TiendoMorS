from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Perfil
from .forms import PefilForm, PerfilUpdateForm, UserForm, UserUpdateForm 
from django.contrib.auth.models import User


# Create your views here.

#### codigo destinado para todo lo que es el registro y logueo
def registrar(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Registro completo! {username} Ya te puedes loguear!')
            return redirect('loguear')
    else:
        form = UserForm(request.POST)
    context = {'form': form}
    return render(request, 'registro/registro.html', context)

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def loguear(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                #return redirect(f'perfil/{request.user.username}')
                return redirect('tienda')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Datos incorrectos")

    form = AuthenticationForm
    context = {'form':form}
    return render(request, "login/login.html", context)


### con este codigo se registra el perfil
def registrarPerfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    if request.method =='POST':
        form = PefilForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.user = current_user
            form.save()
            return redirect('tienda')
    else:
        form = PefilForm()

    context = {'user':user,'form': form}
    return render(request, 'registro/perfil.html', context)

def editar_perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('tienda')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'registro/perfil.html', context)