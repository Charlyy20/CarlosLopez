# Generated by Django 5.0.4 on 2024-04-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreEntrega', '0002_comision'),
    ]

    operations = [
        migrations.AddField(
            model_name='comision',
            name='estudiante',
            field=models.ManyToManyField(to='PreEntrega.estudiante'),
        ),
    ]
