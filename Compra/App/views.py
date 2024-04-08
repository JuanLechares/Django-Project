from django.shortcuts import render
from .models import Proveedor

# Create your views here.

#Productos

def Index(request):
    return render(request, "index.html")

def Producto(request):
    return render(request, "listadoProductos.html")


def ProductosForm(request):
    return render(request, "formProductos.html")

#Proveedores

def Proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listadoProveedores.html", {"proveedores": proveedores})

def ProveedoresForm(request):
    return render(request, "formProveedores.html")

