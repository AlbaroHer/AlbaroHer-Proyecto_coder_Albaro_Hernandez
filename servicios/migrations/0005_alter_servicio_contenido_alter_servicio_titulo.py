# Generated by Django 4.0.4 on 2022-05-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='titulo',
            field=models.CharField(max_length=10),
        ),
    ]
