from django.urls import path
from .views import Producto, Proveedores, ProductosForm, ProveedoresForm
from .views import Proveedores

urlpatterns = [
    path('compra/productos', Producto, name='productos'),
    path('compra/productosForm', ProductosForm, name='productos_form'),
    path('compra/proveedores', Proveedores, name='proveedores'),
    path('compra/proveedoresForm', ProveedoresForm, name='proveedores_form'),
]
