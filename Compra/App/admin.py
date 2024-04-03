from django.contrib import admin
from .models import Producto, Proveedor

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    fields = ["id", "nombre", "apellido", "dni"]
    list_display = ["id", "nombre", "apellido", "dni"]
    
class ProductoAdmin(admin.ModelAdmin):
    fields = ["id","nombre", "precio", "stock_actual", "proveedor"]
    list_display = ["id","nombre", "precio", "stock_actual", "proveedor"]
    
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)