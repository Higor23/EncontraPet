# Generated by Django 3.0.5 on 2020-04-28 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_auto_20200428_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
