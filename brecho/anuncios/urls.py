
from django.urls import path
from.import views

urlpatterns = [
    path('', views.listarAnuncio, name='listar-anuncio'),
    path('areaUsuario/', views.areaUsuario, name='area-usuario'),
    path('addAnuncio/', views.addAnuncio, name='adicionar-anuncio'),
    path('anuncioDetalhado/<int:id>', views.anuncioDetalhado, name='anuncio-detalhado'),
    path('listarCategoria/<int:id>', views.listarCategoria, name='listar-categoria'),
    path('editarAnuncio/<int:id>', views.editarAnuncio, name='editar-anuncio'),
    path('encerrarAnuncio/<int:id>', views.encerrarAnuncio, name='encerrar-anuncio'),
    path('finalizarAnuncio/<int:id>', views.finalizarAnuncio, name='finalizar-anuncio'),
    path('faleConosco/', views.faleConosco, name='fale-conosco'),
    path('msgConfirmacao/', views.msgConfirmacao, name='mensagem-confirmacao'),
    # path('quemSomos/', views.quemSomos, name='quemSomos'),

]
