from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Service(models.Model):
    # Verbose Name="Nombre que se le dara en el administrador y en form html"
    name = models.CharField(null=True, max_length=200, verbose_name="Nombre Servicio")
    description = RichTextField()
    file = models.ImageField(verbose_name="Archivo PDF/CSV/.. etc.", upload_to="archivos", null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True, primary_key=False)
    expiration = models.DateField()
    payday = models.DateField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha De Actualizacion")

    class Meta:
        verbose_name = "servicios"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.name
