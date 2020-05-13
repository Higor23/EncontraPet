from django.db import models
from django.contrib.auth import get_user_model


# class Categoria(models.Model):

#     titulo = models.CharField(max_length=30)

#     def __str__(self):
#         return self.titulo


class Anuncio(models.Model):
    CIDADE = (
        ('Vitória da Conquista - BA', 'Vitória da Conquista - BA'),
    )

    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )

    CATEGORIA = (
        ('Desaparecido', 'Desaparecido'),
        ('Adoção', 'Adoção')
    )

    SEXO = (
        ('Macho', 'Macho'),
        ('Femea', 'Femea')
    )

    ESPECIE = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Pássaro', 'Pássaro'),
    )

    SITUACAO = (
        ('Encontrado', 'Encontrado'),
        ('Adotado', 'Adotado'),
        ('Outro', 'Outro'),
    )
    status = models.CharField(max_length=10, choices=STATUS)
    situacao = models.CharField(max_length=10, choices=SITUACAO, blank=True)
    observacao = models.CharField(max_length=50, blank=True, default="")
    
    categoria = models.CharField(max_length=12, choices=CATEGORIA)
    
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    id = models.BigAutoField(primary_key=True)

    titulo = models.CharField(max_length=28)
    nome_animal = models.CharField(max_length=20, blank=True, default="")
    especie = models.CharField(max_length=8, choices=ESPECIE)
    raca=models.CharField(max_length=20, blank=True, default="")
    sexo_animal = models.CharField(max_length=5, choices=SEXO, blank=True, default="")
    idade_animal = models.CharField(max_length=2, blank=True, default="")
    descricao = models.TextField()
    responsavel = models.CharField(max_length=30, default="")
    whatsApp = models.CharField(max_length=11, blank=True, default="")
    telefone = models.CharField(max_length=11, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    cidade = models.CharField(max_length=30, choices=CIDADE)
    foto_principal = models.FileField(blank=True)
    foto_01 = models.FileField(blank=True)
    foto_02 = models.FileField(blank=True)
    foto_03 = models.FileField(blank=True)
    foto_04 = models.FileField(blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class FaleConosco(models.Model):
    
    nome = models.CharField(max_length=28)
    email = models.CharField(max_length=28)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome