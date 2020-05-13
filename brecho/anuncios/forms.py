from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Anuncio, FaleConosco
from django.utils.translation import gettext_lazy as _



class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = (
            'id',
            'titulo',
            'nome_animal',
            'categoria',
            'especie',
            'raca',
            'sexo_animal',
            'idade_animal',
            'descricao',
            'responsavel',
            'whatsApp',
            'telefone',
            'email',
            'cidade',
            'foto_principal',
            'foto_01',
            'foto_02',
            'foto_03',
            'foto_04'
        )

        labels = {
            'titulo': _('Título Principal'),
            'descricao': _('Descrição'),
            'telefone': _('Telefone'),
            'whatsApp': _('Telefone - WhatsApp'),
            'email': _('Email'),
            'cidade': _('Cidade'),
            'responsavel': _('Responsável'),
            'nome_animal': _('Nome do Pet'),
            'idade_animal': _('Idade do Pet (em anos)'),
            'sexo_animal': _('Sexo do Pet'),
            'especie': _('Espécie'),
            'raca': _('Raça'),
        }


class finalizarForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = (
            'situacao',
            'observacao',
            'status',
        )

        labels = {
            'situacao': _('Situação'),
            'observacao': _('Observações'),
            'status': _('ATENÇÃO: Escolha INATIVO se deseja realmente finalizar o anúncio.')
        }


class FaleConoscoForm(forms.ModelForm):

    class Meta:
        model = FaleConosco
        fields = (
            'nome',
            'mensagem',
            'email',
            
        )

        labels = {
            'nome': _('Nome'),
            'email': _('Email'),
            'mensagem': _('Mensagem'),
        }
