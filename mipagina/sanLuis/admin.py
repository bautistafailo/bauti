from django.contrib import admin

from sanLuis.models import Clientes, Pago, Pedidos

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Pago)
admin.site.register(Pedidos)