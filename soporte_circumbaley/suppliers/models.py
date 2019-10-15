from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Supplier(models.Model):
    # Verbose Name="Nombre que se le dara en el administrador"
    rut = models.CharField(max_length=12)
    name = models.CharField(max_length=20, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['-created']

    def __str__(self):
        return self.name
