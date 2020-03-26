from rest_framework import viewsets
from atracoes.models import Atracao
from atracoes.api.serialize import AtracoesSerialize


class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerialize