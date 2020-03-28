from rest_framework import viewsets
from comentarios.models import Comentario
from comentarios.api.serialize import ComentarioSerialize


class ComentarioViewset(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerialize
