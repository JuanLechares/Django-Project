from django.shortcuts import render, redirect
from .models import Proveedor
from .models import Producto
from django.views.decorators.csrf import csrf_protect

#Productos

def Index(request):
    return render(request, "index.html")

def ProductoListado(request):
    productos = Producto.objects.all()
    return render(request, "listadoProductos.html", {'productos': productos})


def ProductosForm(request):
    
    return render(request, "formProductos.html")

#Proveedores

def ProveedoresListado(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listadoProveedores.html", {"proveedores": proveedores})

@csrf_protect
def ProveedoresForm(request):
    if request.method == 'POST':
        # Si se envió el formulario, obtenemos los datos del formulario del request
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        
        # Creamos una instancia del modelo Proveedor con los datos recibidos
        proveedor = Proveedor(nombre=nombre, apellido=apellido, dni=dni)
        proveedor.save()
        
        # Redireccionamos a alguna página de éxito o hacemos algo más
        return redirect('proveedores') 
    return render(request, "formProveedores.html")

