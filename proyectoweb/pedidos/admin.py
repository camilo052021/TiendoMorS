from django.contrib import admin
from .models import *

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    #search_fields = ('')

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)

