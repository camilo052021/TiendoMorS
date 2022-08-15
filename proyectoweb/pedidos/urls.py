from http.client import ImproperConnectionState
from django. urls import path
from . import views

urlpatterns = [
    path("", views.procesar_pedido, name="procesar_pedido"),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('agregar_pedido/', views.agregar_pedido, name='agregar_pedido'),
    path('editar_pedido/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar_pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),

]