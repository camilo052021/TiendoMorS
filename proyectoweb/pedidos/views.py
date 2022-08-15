from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .forms import LineaPedidoForm


# Create your views here.
@login_required(login_url="/autentication/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "El pedido se procesó correctamente")
    carro.limpiar_carro()
    return redirect('../tienda')

def enviar_mail(**kwargs):
    asunto="gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email="camilo.montoya0531@gmail.com"
    to=kwargs.get("emailusuario")

    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message=mensaje
    )


## este cpdogp es para ver en los templates la lista de os pedidos
def lista_pedidos(request):
    listaPedidos = LineaPedido.objects.all()
    context = {'listaPedidos':listaPedidos}
    return render(request, "pedidos/lista_pedidos.html",context)

@login_required
def agregar_pedido(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = LineaPedidoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('tienda')
        else:
            form = LineaPedidoForm()
        context = {'form':form}
        return render(request, 'pedidos/agregar_pedido.html', context)

@login_required
def editar_pedido(request, id):
    if request.user.is_superuser:
        pedido = get_object_or_404(LineaPedido, pk=id)
        if request.method == 'POST':
            form = LineaPedidoForm(request.POST, instance=pedido)
            if form.is_valid():
                form.save()
                return redirect('lista_pedidos')
        else:
            form = LineaPedidoForm(instance=pedido)  

        context = {'form':form}
        return render(request,'pedidos/editar_pedido.html', context)

@login_required
def eliminar_pedido(request, id):
    if request.user.is_superuser:
        pedido = get_object_or_404(LineaPedido, pk=id)
        pedido.delete()
        return redirect('lista_pedidos')