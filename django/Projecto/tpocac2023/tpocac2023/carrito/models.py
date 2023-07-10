from django.db import models

# Create your models here.

class Carrito(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Precio")
    foto = models.ImageField(upload_to="media",verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    def __str__(self):
        return self.nombre

class Meta:
    verbose_name = "carrito"
    verbose_name_plural = "carritos"
    ordering = ["-created"]
