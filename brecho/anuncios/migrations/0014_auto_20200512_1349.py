# Generated by Django 3.0.5 on 2020-05-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0013_auto_20200511_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='situacao',
            field=models.CharField(choices=[('Encontrado', 'Encontrado'), ('Adotado', 'Adotado'), ('Outro', 'Outro')], max_length=10),
        ),
    ]
