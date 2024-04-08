from django.shortcuts import render
from .models import Proveedor
from .models import Producto
# Create your views here.

#Productos

def Index(request):
    return render(request, "index.html")

def ProductoListado(request):
    productos = Producto.objects.all()
    return render(request, "listadoProductos.html", {'productos': productos})


def ProductosForm(request):
    return render(request, "formProductos.html")

#Proveedores

def Proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listadoProveedores.html", {"proveedores": proveedores})

def ProveedoresForm(request):
    return render(request, "formProveedores.html")

