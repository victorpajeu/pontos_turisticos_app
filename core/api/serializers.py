from rest_framework import serializers
from core.models import PontoTuristico


class PontosTuristicosSerialize(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('pk', 'nome', 'descrição')
