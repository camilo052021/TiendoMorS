from django.urls import path
from django.conf.urls.static import static
from proyectoweb import settings
from django.conf import settings
from . import views

urlpatterns =[
    path('', views.tienda, name='tienda'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),

    ## CRUD categorias
    path('categorias_producto/', views.categorias_producto, name='categorias_producto'),
    path('agregar_categoria_p/', views.agregar_categoria_p, name='agregar_categoria_p'),
    path('editar_categoria_p/<int:id>/', views.editar_categoria_p, name='editar_categoria_p'),
    path('eliminar_categoria_p/<int:id>/', views.eliminar_categoria_p, name='eliminar_categoria_p'),

    ##CRUD PRODUCTOS
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)