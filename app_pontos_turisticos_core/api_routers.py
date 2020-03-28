from rest_framework import routers
from core.api.viewssets import PontosTuristicosViewSet
from atracoes.api.viewset import AtracoeViewSet
from enderecos.api.viewsset import EnderecoViewset

router = routers.DefaultRouter()

router.register('pontos_turisticos', PontosTuristicosViewSet),
router.register('atracoes', AtracoeViewSet)
router.register('enderecos', EnderecoViewset)

rotas_set = router.urls
