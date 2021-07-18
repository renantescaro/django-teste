from django.shortcuts import render
from django.http import HttpResponse


def listar(request):
    context = {
        'pessoas': [
            'Renan',
            'Ana',
            'Luana',
        ],
    }
    return render(request, 'pessoas/listagem.html', context)


def nova(request):
    return HttpResponse('nova pessoa')


def editar(request):
    return HttpResponse('Editar pessoa')