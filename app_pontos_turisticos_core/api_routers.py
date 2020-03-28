from rest_framework import routers
from core.api.viewssets import PontosTuristicosViewSet
from atracoes.api.viewset import AtracoesViewSet
from enderecos.api.viewsset import EnderecosViewset

router = routers.DefaultRouter()

router.register('pontos_turisticos', PontosTuristicosViewSet),
router.register('atracoes', AtracoesViewSet)
router.register('enderecos', EnderecosViewset)

rotas_set = router.urls
