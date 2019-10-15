# Generated by Django 2.2.5 on 2019-10-13 00:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('content', models.TextField(blank=True, null=True, verbose_name='contenido')),
                ('image', models.ImageField(upload_to='services', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha De Actualizacion')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['-created'],
            },
        ),
    ]
