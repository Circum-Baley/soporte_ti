# Generated by Django 2.2.5 on 2019-10-08 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upland_to, verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='BioModel')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('department_profile', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]
