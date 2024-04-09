from django.urls import path
from .views import ProductoListado, ProveedoresListado, ProductosForm, ProveedoresForm, Index

urlpatterns = [
    path('', Index, name='inicio'),
    path('compra/productos', ProductoListado, name='productos'),
    path('compra/productosForm', ProductosForm, name='productos_form'),
    path('compra/proveedores', ProveedoresListado, name='proveedores'),
    path('compra/proveedoresForm', ProveedoresForm, name='proveedores_form'),
]
