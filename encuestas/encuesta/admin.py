from django.contrib import admin

from .models import (
    Ciudad,
    DatosEncuestado,
    Pregunta,
    OpcionRespuesta,
    Respuesta,
    Encuesta
)

class OpcionRespuestaInline(admin.TabularInline):
    model = OpcionRespuesta

class EncuestasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'fecha_desde')
    search_fields = ('nombre', 'slug')
    list_filter = ('slug', 'fecha_desde',)

class DatosEncuestadoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'ciudad', 'email')
    search_fields = ('nombres', 'apellidos', 'ciudad')
    list_filter = ('ciudad', 'encuesta',)
    raw_id_fields = ('encuesta',)

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('encuesta', 'nombre', 'descripcion', 'respuestas_multiples')
    search_fields = ('encuesta', 'nombre', 'descripcion')
    list_filter = ('encuesta', 'nombre',)
    raw_id_fields = ('encuesta',)
    inlines = [
        OpcionRespuestaInline,
    ]

class OpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'titulo')
    search_fields = ('pregunta', 'titulo')
    list_filter = ('pregunta',)
    raw_id_fields = ('pregunta',)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('encuestado', 'pregunta', 'detalle_respuesta')
    search_fields = ('encuestado', 'pregunta')
    list_filter = ('pregunta', 'encuestado',)
    raw_id_fields = ('pregunta',)


admin.site.register(Encuesta, EncuestasAdmin)
admin.site.register(Ciudad)
admin.site.register(DatosEncuestado, DatosEncuestadoAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(OpcionRespuesta, OpcionRespuestaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
