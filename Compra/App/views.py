from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, "index.html")

def Producto(request):
    return render(request, "listadoProductos.html")

def Proveedores(request):
    return render(request, "listadoProveedores.html")