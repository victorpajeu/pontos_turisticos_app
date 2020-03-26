from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontosTuristicosSerialize


class PontosTuristicosViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontosTuristicosSerialize
