from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Document(models.Model):
    types = models.CharField(max_length=30, verbose_name="Tipo De Documento")
    number = models.BigIntegerField(primary_key=False, verbose_name="Numero De Documento")
    description = RichTextField(null=True, blank=True)
    payday = models.DateField(verbose_name="Dia De Pago")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")
    expiration = models.DateField(verbose_name="Vencimiento")
    # amount = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Monto")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['-created']

    def __str__(self):
        return self.types
