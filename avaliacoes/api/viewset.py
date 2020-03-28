from rest_framework import viewsets
from avaliacoes.models import Avaliacoes
from avaliacoes.api.serialize import AvaliacaoSerialize


class AvaliacaoViewset(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerialize
