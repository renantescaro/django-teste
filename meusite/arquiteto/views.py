from django.http.request import HttpRequest
from django.shortcuts import render
from .forms import ArquitetoForm
from .models import Arquiteto


def listar(request:HttpRequest):
    context = {}
    form = ArquitetoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'listagem.html', context)