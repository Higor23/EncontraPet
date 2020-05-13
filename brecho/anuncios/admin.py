from django.contrib import admin
from .models import Anuncio


class detalhesAnuncio(admin.ModelAdmin):

    list_display=('titulo', 'id','user', 'status', 'categoria', 'cidade', 'created_at', 'updated_at','situacao')
    
    search_fields = ['titulo']

admin.site.register(Anuncio, detalhesAnuncio)






