from rest_framework import routers
from core.api.viewssets import PontosTuristicosViewSet

router = routers.DefaultRouter()

router.register('pontos_turisticos', PontosTuristicosViewSet)

rotas_set = router.urls