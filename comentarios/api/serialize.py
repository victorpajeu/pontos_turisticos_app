from rest_framework import serializers
from comentarios.models import Comentario


class ComentarioSerialize(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('user', 'comentario', 'aprovado', 'data')
