# Generated by Django 2.2.5 on 2019-10-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Fecha De Creacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Actualizacion')),
                ('suppliers', models.CharField(max_length=20, verbose_name='Proveedor')),
                ('description', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='services', verbose_name='imagen')),
                ('quantity', models.IntegerField(max_length=1, verbose_name='Cantidad')),
            ],
        ),
    ]
