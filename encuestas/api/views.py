from rest_framework import viewsets, mixins
from encuestas.encuesta.models import Pregunta, Encuesta
from .serializers import PreguntaModelSerializer, EncuestaModelSerializer

class PreguntasViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaModelSerializer

class EncuestaViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaModelSerializer
    lookup_field = 'slug'
    