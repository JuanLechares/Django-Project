from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, "index.html")

def Producto(request):
    return HttpResponse("listado de productos")

def Proveedores(request):
    return HttpResponse("listado de proveedores")