# Generated by Django 3.0.5 on 2020-05-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0006_auto_20200428_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=10),
        ),
    ]