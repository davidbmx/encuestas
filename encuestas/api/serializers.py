from rest_framework import serializers
from encuestas.encuesta.models import Pregunta, OpcionRespuesta, Encuesta, Ciudad, Respuesta, DatosEncuestado
from django.shortcuts import get_object_or_404

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
            'dependencia', 'especifica'
        ]

class EncuestaModelSerializer(serializers.ModelSerializer):
    preguntas = PreguntaModelSerializer(many=True)

    class Meta:
        model = Encuesta
        fields = [
            'nombre', 'descripcion', 'slug',
            'fecha_desde','fecha_hasta', 'preguntas'
        ]

class CiudadModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = '__all__'

class DatosEncuestaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosEncuestado
        fields = '__all__'

class RespuestaSave(serializers.Serializer):
    id_pregunta = serializers.IntegerField()
    id_opcion = serializers.CharField(required=False, allow_blank=True)
    texto_respuesta = serializers.CharField(required=False, allow_blank=True)
    relacion_pregunta = serializers.CharField(required=False, allow_blank=True)

class DatosEncuestadoSave(serializers.Serializer):
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    edad = serializers.IntegerField()
    genero = serializers.CharField()
    ciudad = serializers.IntegerField()
    email = serializers.EmailField()
    tiene_hijos = serializers.BooleanField()
    edad_hijos = serializers.CharField(allow_blank=True)

class DatosEncuestadoModel(serializers.ModelSerializer):
    class Meta:
        model = DatosEncuestado
        fields = '__all__'



class RespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respuesta
        fields = '__all__'

class RespuestaGuardar(serializers.Serializer):
    id_encuesta = serializers.CharField()
    respuestas = RespuestaSave(many=True, read_only=False)
    datos_encuestado = DatosEncuestadoSave(many=False, read_only=False)

    # def save(self):
    #     print(self.validated_data['id_encuesta'])

    def save(self):
        data = self.validated_data
        encuesta = get_object_or_404(Encuesta, slug=data['id_encuesta'])
        datos_encuestado = data['datos_encuestado']
        data_enc = {
            'encuesta': encuesta.id,
            'nombres':datos_encuestado['nombres'],
            'apellidos': datos_encuestado['apellidos'],
            'edad': datos_encuestado['edad'],
            'genero': datos_encuestado['genero'],
            'ciudad': datos_encuestado['ciudad'],
            'email': datos_encuestado['email'],
            'tiene_hijos': datos_encuestado['tiene_hijos'],
            'edad_hijos': datos_encuestado['edad_hijos']
        }
        encuestado = DatosEncuestadoModel(data=data_enc)
        if not encuestado.is_valid(): 
            print()
        encuestado.save()

        respuestas = data['respuestas']
        for respuesta in respuestas:
            id_opcion = respuesta['id_opcion']
            relacion_pregunta = respuesta['relacion_pregunta']
            data = {
                'encuestado': encuestado.data.get('id'),
                'pregunta': respuesta['id_pregunta'],
                'detalle_respuesta': respuesta['texto_respuesta']
            }
            if int(id_opcion) != 0:
                data['opcion_respuesta'] = id_opcion
            
            if int(relacion_pregunta) != 0:
                data['relacion_pregunta'] = relacion_pregunta

            serializer = RespuestaSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.errors)

            serializer.save()
        


    

