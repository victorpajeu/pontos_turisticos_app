from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacoes
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField('nome', max_length=100)
    descrição = models.TextField('descrição')
    aprovado = models.BooleanField('aprovado')
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacoes)
    enderoco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
