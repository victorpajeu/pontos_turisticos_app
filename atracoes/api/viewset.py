from rest_framework import viewsets
from atracoes.models import Atracao
from atracoes.api.serialize import AtracoesSerialize


class AtracoeViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerialize