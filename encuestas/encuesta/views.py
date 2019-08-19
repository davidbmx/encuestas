from django.shortcuts import render

from .models import Encuesta, Pregunta, OpcionRespuesta
from encuestas.api.serializers import EncuestaModelSerializer

def encuesta(request):
    return render(request, 'encuestas/index.html')

def encuestaUno(request):
    return render(request, 'encuestas/encuestaUno.html', {})