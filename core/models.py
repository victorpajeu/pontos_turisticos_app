from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField('nome', max_length=100)
    descrição = models.TextField('descrição')
    aprovado = models.BooleanField('status')

    def __str__(self):
        return self.nome
