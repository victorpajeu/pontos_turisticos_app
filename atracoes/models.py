from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField('descricão')
    horario_de_func = models.TextField()
    idade_min = models.IntegerField('Idade de minima')

    def __str__(self):
        return self.nome

