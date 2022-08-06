from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from proyectoweb import settings
from . import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('editar_servicio/<int:id>/', views.editar_servicio, name = 'editar_servicio'),
    path('eliminar_servicio/<int:id>/', views.eliminar_servicio, name = 'eliminar_servicio'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)