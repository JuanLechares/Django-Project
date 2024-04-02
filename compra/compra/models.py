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
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
    
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    precio = models.FloatField(verbose_name="Precio")
    stock_actual = models.IntegerField(verbose_name="Stock")
    class Meta:
        db_table = "Productores"
        verbose_name="Productor"
        verbose_name_plural="Productores" 
        
    def __str__(self):
        return f"{self.nombre} - $ {self.precio} - STOCK: {self.stock_actual}"
