from django.urls import path
from .views import Producto
from .views import Proveedores

urlpatterns = [
    path('compra/productos', Producto),
    path('compra/proveedores', Proveedores),
]
