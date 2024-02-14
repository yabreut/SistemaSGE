# Generated by Django 4.0.6 on 2023-04-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_entidad_ruta_alter_entidad_acceso'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='rutamanual',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='acceso',
            field=models.CharField(choices=[('CITRIX', 'Citrix'), ('CORREO', 'Correo'), ('DESKTOP', 'Desktop'), ('WEB', 'Web')], max_length=50, null=True),
        ),
    ]
