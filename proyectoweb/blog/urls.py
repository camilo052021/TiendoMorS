from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from proyectoweb import settings
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('agregar_post', views.agregar_post, name='agregar_post'),
    path('editar_post/<int:id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:id>/', views.eliminar_post, name='eliminar_post'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)