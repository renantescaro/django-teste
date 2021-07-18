from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def listar(request):
    context = {
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'pessoas/listagem.html', context)


def nova(request):
    return render(request, 'pessoas/formulario.html', {})


def editar(request, pessoa_id):
    context = {
        'pessoa': Pessoa.objects.get(pk=pessoa_id)
    }
    return render(request, 'pessoas/formulario.html', context)