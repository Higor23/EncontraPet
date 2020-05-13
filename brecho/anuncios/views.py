from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnuncioForm, finalizarForm, FaleConoscoForm
from .models import Anuncio
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django. conf import settings

def listarCategoria(request, pk_test):

    categoria = Anuncio.objects.get(id=pk_test)
    orders = Anuncio.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'categoria': categoria, 'orders': orders,
               'order_count': order_count, 'myFilter': myFilter}

    return render(request, 'anuncios/listarAnuncio.html', {'anuncios': anuncios})


def areaUsuario(request):

    anuncios = Anuncio.objects.all().order_by(
        '-created_at').filter(user=request.user)

    anuncios = Anuncio.objects.all().order_by(
        '-created_at').filter(user=request.user)

    return render(request, 'anuncios/areaUsuario.html', {'anuncios': anuncios})


def listarAnuncio(request):
    # Busca

    search = request.GET.get('search')

    # Filter
    filter = request.GET.get('filter')

    if search:
        anuncios = Anuncio.objects.filter(
            titulo__icontains=search, status='Ativo')
    # elif filter:
    #     anuncios = Anuncio.objects.filter(status='ativo')
    elif filter:
        anuncios = Anuncio.objects.filter(categoria=filter)
    else:
        anuncios_list = Anuncio.objects.all().order_by('-created_at')
        paginator = Paginator(anuncios_list, 8)

        page = request.GET.get('page')

        anuncios = paginator.get_page(page)

    return render(request, 'anuncios/listarAnuncio.html', {'anuncios': anuncios})


@login_required
def areaUsuario(request):

    anuncios = Anuncio.objects.all().order_by(
        '-created_at').filter(user=request.user)

    anuncios = Anuncio.objects.all().order_by(
        '-created_at').filter(user=request.user)

    return render(request, 'anuncios/areaUsuario.html', {'anuncios': anuncios})


def anuncioDetalhado(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    return render(request, 'anuncios/anuncioDetalhado.html', {'anuncio': anuncio})


@login_required
def addAnuncio(request):

    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)

        if form.is_valid():
            Anuncio = form.save(commit=False)
            Anuncio.status = 'Ativo'
            Anuncio.user = request.user
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = AnuncioForm()
    return render(request, 'anuncios/addAnuncio.html', {'form': form})

# Se o usuário não está logado, impede que seja visualizado por qualquer um.
@login_required
def editarAnuncio(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    form = AnuncioForm(instance=anuncio)

    if(request.method == 'POST'):
        form = AnuncioForm(request.POST, instance=anuncio)

        if(form.is_valid()):
            anuncio.save()
            return redirect('/')
        else:
            return render(request, 'anuncios/editarAnuncio.html', {'form': form, 'anuncio': anuncio})

    else:
        return render(request, 'anuncios/editarAnuncio.html', {'form': form, 'anuncio': anuncio})


@login_required
def finalizarAnuncio(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)

    if(anuncio.status == 'Ativo'):
        anuncio.status = 'Inativo'
    else:
        anuncio.status = 'Inativo'
    anuncio.save()

    return redirect('/areaUsuario/')


@login_required
def encerrarAnuncio(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    form = finalizarForm(instance=anuncio)

    if(request.method == 'POST'):
        form = finalizarForm(request.POST, instance=anuncio)

        if(form.is_valid()):
            anuncio.save()
            
            return redirect('/areaUsuario/')

        else:
            return render(request, 'anuncios/encerrarAnuncio.html', {'form': form, 'anuncio': anuncio})

    else:
        return render(request, 'anuncios/encerrarAnuncio.html', {'form': form, 'anuncio': anuncio})


def faleConosco(request):
    
    if (request.method == 'POST'):
        
        form = FaleConoscoForm(request.POST)
        nome = request.POST.get('nome', '')
        mensagem = request.POST.get('mensagem', '')
        email = request.POST.get('email', '')
        

        if form.is_valid():

            send_mail(nome, mensagem, email, ['desenvolvedor.higor@gmail.com'], fail_silently=False)
    
            # return redirect('/msgConfirmacao/')
            return render(request, 'anuncios/msgConfirmacao.html', {'form':form})
        
    else:
        
        form=FaleConoscoForm()
    return render(request, 'anuncios/faleConosco.html', {'form':form})


def msgConfirmacao(request):

    return redirect('/')

    
# def faleConosco(request):

#     if request.method == 'POST':
#         form = AnuncioForm(request.POST, request.FILES)

#         if form.is_valid():
#             Anuncio = form.save(commit=False)
#             Anuncio.status = 'Ativo'
#             Anuncio.user = request.user
#             form.save()
#             return HttpResponseRedirect('/')

#     else:
#         form = AnuncioForm()
#     return render(request, 'anuncios/addAnuncio.html', {'form': form})