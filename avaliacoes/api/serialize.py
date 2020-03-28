from rest_framework import serializers
from avaliacoes.models import Avaliacoes


class AvaliacaoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('user', 'comentario', 'nota', 'aprovado', 'data')
