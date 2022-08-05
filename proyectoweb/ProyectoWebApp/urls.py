from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

from proyectoweb.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns =[
    path('', views.home, name='home'),
    
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)