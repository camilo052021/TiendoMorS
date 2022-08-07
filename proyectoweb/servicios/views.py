from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from servicios.models import Servicio
from .forms import ServicioForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios':servicios}
    return render(request, "servicios/servicios.html",context)

@login_required
def agregar_servicio(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ServicioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('servicios')
        else:
            form = ServicioForm()

        context = {'form':form}
        return render(request, 'servicios/agregar_servicio.html', context)

@login_required
def editar_servicio(request, id):
    if request.user.is_superuser:
        servicio = get_object_or_404(Servicio, pk=id)
        if request.method == 'POST':
            form = ServicioForm(request.POST, instance=servicio)
            if form.is_valid():
                form.save()
                return redirect('servicios')
        else:
            form = ServicioForm(instance=servicio)
        
        context = {'form':form}
        return render(request,'servicios/editar_servicio.html', context)

@login_required
def eliminar_servicio(request, id):
    if request.user.is_superuser:
        servicio = get_object_or_404(Servicio, pk=id)
        servicio.delete()
        return redirect('servicios')