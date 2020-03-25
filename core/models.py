from django.db import models
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    nome = models.CharField('nome', max_length=100)
    descrição = models.TextField('descrição')
    aprovado = models.BooleanField('aprovado')
    atracao = models.ManyToManyField(Atracao)

    def __str__(self):
        return self.nome
