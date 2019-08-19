from rest_framework import viewsets, mixins
from encuestas.encuesta.models import Pregunta, Encuesta, Ciudad
from .serializers import PreguntaModelSerializer, EncuestaModelSerializer, CiudadModelSerializer, RespuestaGuardar

class PreguntasViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaModelSerializer

class EncuestaViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaModelSerializer
    lookup_field = 'slug'

class CiudadViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadModelSerializer

class RespuestaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RespuestaGuardar
    