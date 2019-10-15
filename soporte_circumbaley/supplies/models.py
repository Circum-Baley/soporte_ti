from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Supply(models.Model):
    # Verbose Name="Nombre que se le dara en el administrador"
    name = models.CharField(max_length=20, verbose_name="Nombre")
    departments = models.CharField(null=True, blank=True, max_length=30, verbose_name="Departamento")
    suppliers = models.CharField(max_length=20, verbose_name="Proveedor")
    description = RichTextField(verbose_name="Descripcion")
    quantity = models.IntegerField(default=2, verbose_name="Cantidad")
    image = models.ImageField(verbose_name="imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")

    # numDocument = models.CharField(max_length=10)


class Meta:
    verbose_name = "Insumo"
    verbose_name_plural = "Insumos"
    ordering = ['-created']


def __str__(self):
    return self.name
