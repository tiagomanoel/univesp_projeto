from django.shortcuts import render, get_object_or_404, redirect
from .models import law
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import os





def index(request):
    List_l = law.objects.all().order_by('-id_law')
    busca = request.GET.get('busca')
    if busca:
        List_l = law.objects.filter(texto__icontains = busca)
        paginator = Paginator(List_l, 6)
        pages = request.GET.get('pages')
        List = paginator.get_page(pages)
        return render(request, 'index.html', {'List': List})
    paginator = Paginator(List_l, 10)
    pages = request.GET.get('pages')
    List = paginator.get_page(pages)
    return render(request, 'index.html', {'List': List})

def about(request):
    return render(request, 'about.html')

@login_required
def form(request):
    List_l = law.objects.all().order_by('-id_law')
    if request.method == "POST":
        file = request.FILES.get("my_file")
        mf = law(title ="File", arq=file, numero = request.POST.get('numero'), ano = request.POST.get('ano'), situacao = request.POST.get('situacao'), texto = request.POST.get('texto'))
        mf.save()
        messages.info(request, 'Cadastrado com sucesso.')
        return redirect('/form/insert')
    paginator = Paginator(List_l, 8)
    pages = request.GET.get('pages')
    List = paginator.get_page(pages)
    return render(request, 'form.html', {'List': List})
@login_required
def delete(request, id_law):
    dado = get_object_or_404(law, pk=id_law)
    file = dado.arq
    location = "/home/tiagomanoel/Documentos/projeto/univesp/core/media/"
    if file:
        os.remove(f'{location}{file}')
    dado.delete()
    messages.info(request, 'Dados deletados com sucesso.')
    return redirect('/form/')
@login_required
def insert(request):
    return render(request, 'insert.html')




  