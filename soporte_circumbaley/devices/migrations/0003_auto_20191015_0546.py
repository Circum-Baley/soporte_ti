# Generated by Django 2.2.5 on 2019-10-15 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20191015_0545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='is_true',
            new_name='is_new',
        ),
    ]
