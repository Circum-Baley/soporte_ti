from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Devices(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripción")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(verbose_name="Fecha De Creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha De Actualizacion", auto_now=True)
    is_new = models.BooleanField(verbose_name="tiene Respaldo (Boleta-Factura)?")

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
