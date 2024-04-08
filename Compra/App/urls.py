from django.urls import path
from .views import ProductoListado, Proveedores, ProductosForm, ProveedoresForm

urlpatterns = [
    path('compra/productos', ProductoListado, name='productos'),
    path('compra/productosForm', ProductosForm, name='productos_form'),
    path('compra/proveedores', Proveedores, name='proveedores'),
    path('compra/proveedoresForm', ProveedoresForm, name='proveedores_form'),
]
