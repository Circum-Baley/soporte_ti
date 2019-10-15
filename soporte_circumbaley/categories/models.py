from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    level = models.IntegerField(default=0, verbose_name="level")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha De Creacion")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Actualizacion")
    description = models.CharField(max_length=300, verbose_name="Descripcion")
    image = models.ImageField(verbose_name="imagen", upload_to="services")


class Meta:
    verbose_name = "Categoria"
    verbose_name_plural = "Categorias"
    ordering = ['-created']


def __str__(self):
    return self.name
