from rest_framework import viewsets
from enderecos.models import Endereco
from enderecos.api.serialize import EnderecosSerialize


class EnderecosViewset(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerialize
