"""proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('servicios/', include('servicios.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('', include('ProyectoWebApp.urls')),
    #path('accounts/', include('django.contrib.auth.urls')), borrar esta linea
path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), 
        name='reset_password'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), 
        name='password_reset_complete'),

]
