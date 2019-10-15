# Generated by Django 2.2.5 on 2019-10-08 05:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha De Actualizacion')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['created'],
            },
        ),
    ]