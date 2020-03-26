from rest_framework import serializers
from atracoes.models import Atracao


class AtracoesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('pk', 'nome', 'descricao',)
