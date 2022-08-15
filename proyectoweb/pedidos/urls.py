from http.client import ImproperConnectionState
from django. urls import path
from . import views

urlpatterns = [
    path("", views.procesar_pedido, name="procesar_pedido"),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),

]