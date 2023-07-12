from django.contrib import admin
from .models import Modalidad, Pago, Clientes, Pedidos, Accounts, Accounts2

@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo', 'autor', 'fecha']
    search_fields = ['titulo', 'subtitulo', 'contenido']
    list_filter = ['autor', 'fecha']

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'seccion', 'precio']

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono']

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ['numero', 'fecha', 'pagado']

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']

@admin.register(Accounts2)
class Accounts2Admin(admin.ModelAdmin):
    list_display = ['user']
