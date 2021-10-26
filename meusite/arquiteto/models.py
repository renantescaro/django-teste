from django.db import models
from pessoas.models import Pessoa


class Arquiteto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cau    = models.CharField(max_length=200)

    def __str__(self) -> str:
        return super().__str__()