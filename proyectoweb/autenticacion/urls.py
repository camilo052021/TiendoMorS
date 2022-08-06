from django.urls import path
from .views import VRegistro, cerrar_sesion, loguear
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('loguear', loguear, name='loguear'), 
]
