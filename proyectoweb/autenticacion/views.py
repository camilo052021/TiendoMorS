from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

class VRegistro(View):

    def get(slef,request):
        form = UserCreationForm()
        context = {'form':form}
        return render(request, "registro/registro.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            context = {'form':form}
            return render(request, "registro/registro.html", context)

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
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Datos incorrectos")

    form = AuthenticationForm
    context = {'form':form}
    return render(request, "login/login.html", context)
    