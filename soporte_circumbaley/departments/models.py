from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripcion")
    address = models.CharField(max_length=200, verbose_name="Direccion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['created']

    def __str__(self):
        return self.name
