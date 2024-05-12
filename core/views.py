from django.shortcuts import render
from .models import law
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    List = law.objects.all()
    busca = request.GET.get('busca')
    if busca:
        List = law.objects.filter(texto__icontains = busca)
    
    return render(request, 'index.html', {'List': List})

def about(request):
    return render(request, 'about.html')

@login_required
def form(request):
    if request.method == "GET":
        return render(request, "form.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        mf = law(title ="File", arq=file, numero = request.POST.get('numero'), ano = request.POST.get('ano'), situacao = request.POST.get('situacao'), texto = request.POST.get('texto'))
        mf.save()
    return render(request, 'form.html')
