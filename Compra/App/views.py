from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, "index.html")

def Producto(request):
    return render(request, "listadoProductos.html")

def Proveedores(request):
    return render(request, "listadoProveedores.html")

def ProductosForm(request):
    return render(request, "formProductos.html")

def ProveedoresForm(request):
    return render(request, "formProveedores.html")