from django.db import models
from encuestas.utils.models import AbstractModel

class Ciudad(AbstractModel):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Encuesta(AbstractModel):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    valida_edad = models.BooleanField(default=False)
    edad_desde = models.IntegerField(default=0)
    edad_hasta = models.IntegerField(default=0)
    fecha_desde = models.DateTimeField()
    fecha_hasta = models.DateTimeField()

    def __str__(self):
        return self.nombre


class DatosEncuestado(AbstractModel):
    GENEROS = (
        ('H', 'HOMBRE'),
        ('M', 'MUJER'),
    )
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, null=True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=GENEROS, default='H')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    tiene_hijos = models.BooleanField(default=False)
    edad_hijos = models.CharField(max_length=100, null=True, blank=True)
    genero_hijo = models.CharField(max_length=1, choices=GENEROS, default='H')

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)


class Pregunta(AbstractModel):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, null=True, related_name='preguntas')
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=150)
    respuestas_multiples = models.BooleanField(default=False)
    max_respuestas = models.PositiveIntegerField(default=0)
    tipo_respuesta = models.CharField(max_length=10)
    dependencia = models.ForeignKey('encuesta.Pregunta', on_delete=models.SET_NULL, blank=True, null=True)
    especifica = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='preguntas/', blank=True, null=True)

    class Meta(AbstractModel.Meta):
        ordering = ['id']

    def __str__(self):
        return self.nombre

class OpcionRespuesta(AbstractModel):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    titulo = models.CharField(max_length=150, blank=True, null=True)
    especifica = models.BooleanField(default=False)
    genero = models.CharField(max_length=1, default='N')
    imagen = models.ImageField(upload_to='opciones_respuestas/', blank=True, null=True)

    class Meta(AbstractModel.Meta):
        ordering = ['id']

    def __str__(self):
        return self.pregunta.nombre
    

class Respuesta(AbstractModel):
    encuestado = models.ForeignKey(DatosEncuestado, on_delete=models.CASCADE, related_name='respuesta')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuesta_pregunta')
    relacion_pregunta = models.ForeignKey(Pregunta, on_delete=models.SET_NULL, blank=True, null=True, related_name='respuesta_relacionada')
    opcion_respuesta = models.ForeignKey(
        OpcionRespuesta,
        on_delete=models.SET_NULL,
        blank=True,null=True
    )
    detalle_respuesta = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.detalle_respuesta



