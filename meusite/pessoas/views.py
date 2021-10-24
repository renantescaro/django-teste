from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from .models import Pessoa


def listar(request:HttpRequest):
    context = {
        'pessoas': Pessoa.objects.all(), }
    return render(request, 'listagem.html', context)


def nova(request:HttpRequest):
    return render(request, 'formulario.html', {})


def editar(request:HttpRequest, pessoa_id:int):
    context = {
        'pessoa': Pessoa.objects.get(pk=pessoa_id) }
    return render(request, 'formulario.html', context)


def salvar(request:HttpRequest):
    if request.method == 'POST':
        # inserir
        if request.POST.get('id') is None:
            Pessoa(
                nome     = request.POST.get('nome'),
                email    = request.POST.get('email'),
                telefone = request.POST.get('telefone'),
            ).save()
            return redirect('/pessoas')
        
        # editar
        pessoa:Pessoa   = Pessoa.objects.get(pk=int(request.POST.get('id')))
        pessoa.nome     = request.POST.get('nome')
        pessoa.email    = request.POST.get('email')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.save()
    return redirect('/pessoas')


def apagar(request:HttpRequest, pessoa_id:int):
    if pessoa_id is not None:
        Pessoa.objects.filter(pk=pessoa_id).delete()
    return redirect('/pessoas')