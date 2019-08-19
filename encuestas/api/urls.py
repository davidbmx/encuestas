from rest_framework.routers import DefaultRouter

from .views import PreguntasViewSet, EncuestaViewSet, CiudadViewSet, RespuestaViewSet

router = DefaultRouter()
router.register(r'preguntas', PreguntasViewSet, basename='preguntas')
router.register(r'encuestas', EncuestaViewSet, basename='encuestas')
router.register(r'ciudades', CiudadViewSet, basename='ciudades')
router.register(r'respuestas', RespuestaViewSet, basename='respuestas')

urlpatterns = router.urls
