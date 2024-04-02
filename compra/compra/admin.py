from django.contrib import admin
from .models import Producto, Proveedor

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", "dni"]
    list_display = ["nombre", "apellido", "dni"]
    
admin.site.register(Proveedor, ProveedorAdmin)