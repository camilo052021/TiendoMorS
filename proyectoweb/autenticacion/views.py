from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Perfil
from .forms import PefilForm, UserForm 
from django.contrib.auth.models import User


# Create your views here.

# class VRegistro(View):

#     def get(self,request):
#         form = UserCreationForm()
#         context = {'form':form}
#         return render(request, "registro/registro.html", context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             usuario = form.save()
#             login(request, usuario)
#             return redirect('home')
#         else:
#             for msg in form.error_messages:
#                 messages.error(request, form.error_messages[msg])

#             context = {'form':form}
#             return render(request, "registro/registro.html", context)#


#### codigo destinado para todo lo que es el registro y logueo
def registrar(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Registro completo! Ya te puedes loguear!')
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
                return redirect(f'registrarPerfil/{request.user.id}')
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
    context = {'user':user}
    return render(request, 'registro/perfil.html', context)
    