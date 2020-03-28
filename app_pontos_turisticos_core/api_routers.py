from rest_framework import routers
from core.api.viewssets import PontosTuristicosViewSet
from atracoes.api.viewset import AtracoeViewSet
from enderecos.api.viewsset import EnderecoViewset
from comentarios.api.viewset import ComentarioViewset
from avaliacoes.api.viewset import AvaliacaoViewset

router = routers.DefaultRouter()
router.register('pontos_turisticos', PontosTuristicosViewSet)
router.register('atracoes', AtracoeViewSet)
router.register('enderecos', EnderecoViewset)
router.register('comentarios', ComentarioViewset)
router.register('avaliações', AvaliacaoViewset)

rotas_set = router.urls
