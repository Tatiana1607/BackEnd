from django.contrib import admin
from .models import Cliente, Empleado, OrdenCompra, EstadoCompra

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(OrdenCompra)
admin.site.register(EstadoCompra)