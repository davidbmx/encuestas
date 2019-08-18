from rest_framework import serializers
from encuestas.encuesta.models import Pregunta, OpcionRespuesta, Encuesta

class OpcionRespuesta(serializers.ModelSerializer):

    class Meta:
        model = OpcionRespuesta
        fields = '__all__'

class PreguntaModelSerializer(serializers.ModelSerializer):
    opciones = OpcionRespuesta(many=True)
    
    class Meta:
        model = Pregunta
        fields = [
            'id', 'nombre', 'descripcion',
            'respuestas_multiples', 'max_respuestas',
            'tipo_respuesta', 'imagen', 'opciones',
            'dependencia'
        ]

class EncuestaModelSerializer(serializers.ModelSerializer):
    preguntas = PreguntaModelSerializer(many=True)

    class Meta:
        model = Encuesta
        fields = [
            'nombre', 'descripcion', 'slug',
            'fecha_desde','fecha_hasta', 'preguntas'
        ]

