# Generated by Django 2.2.5 on 2019-10-15 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='es_nuevo',
            new_name='is_true',
        ),
    ]