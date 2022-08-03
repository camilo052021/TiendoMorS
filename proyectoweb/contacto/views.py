from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from proyectoweb import settings

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            email=EmailMessage(
                    "Mensaje:Mensaje desde Django",
                    "El usuario {} del correo {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
                    #settings.EMAIL_HOST_USER, 
                    ['camilo.montoya0531@gmail.com'], 
                    reply_to=[email]
                    )	

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?envionovalido")

    context={'formulario_contacto':formulario_contacto}
    return render(request, "contacto/contacto.html", context)
