from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellido", max_length=100)
    dni = models.IntegerField(verbose_name="Dni", validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
    
    class Meta:
        db_table = "Proveedores"
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores" 
        
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    precio = models.DecimalField(verbose_name="Precio", max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField(verbose_name="Stock")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
    class Meta:
        db_table = "Productos"
        verbose_name="Producto"
        verbose_name_plural="Productos" 
        
    def __str__(self):
        return f"{self.nombre}"