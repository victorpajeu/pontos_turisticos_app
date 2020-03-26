from rest_framework import routers
from core.api.viewssets import PontosTuristicosViewSet
from atracoes.api.viewset import AtracoesViewSet

router = routers.DefaultRouter()

router.register('pontos_turisticos', PontosTuristicosViewSet),
router.register('atracoes', AtracoesViewSet)

rotas_set = router.urls
