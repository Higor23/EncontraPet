# Generated by Django 3.0.5 on 2020-04-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='categoria',
            field=models.CharField(choices=[('Calçados', 'Calçados'), ('Roupas', 'Roupas'), ('Acessórios', 'Acessórios'), ('Outros', 'Outros')], max_length=10),
        ),
    ]