# Generated by Django 4.0.6 on 2023-04-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_entidad_rutamanual_alter_entidad_acceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='ruta',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='rutamanual',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
