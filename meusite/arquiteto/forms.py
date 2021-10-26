from django import forms
from django.db.models import fields
from .models import Arquiteto as ArquitetoModel


class ArquitetoForm(forms.ModelForm):
    class Meta:
        model  = ArquitetoModel
        fields = '__all__'