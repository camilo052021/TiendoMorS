from django.urls import path
from .views import registrar, cerrar_sesion, loguear, registrarPerfil
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', registrar, name='autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('loguear', loguear, name='loguear'), 

    ## registro del perfil
    path('registrarPerfil', registrarPerfil, name='registrarPerfil'), 
]
