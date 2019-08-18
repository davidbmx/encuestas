from django.shortcuts import render

from .models import Encuesta, Pregunta, OpcionRespuesta

def encuesta(request):
    
    return render(request, 'encuestas/encuesta.html')