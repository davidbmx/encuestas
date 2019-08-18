from rest_framework.routers import DefaultRouter

from .views import PreguntasViewSet, EncuestaViewSet

router = DefaultRouter()
router.register(r'preguntas', PreguntasViewSet, basename='preguntas')
router.register(r'encuestas', EncuestaViewSet, basename='encuestas')

urlpatterns = router.urls
