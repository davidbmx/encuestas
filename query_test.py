from encuestas.encuesta.models import DatosEncuestado, Respuesta

# datos = Respuesta.objects.filter(encuestado__nombres='Pedro')

# for d in datos:
#     print('-'.join(['' for i in range(30)]))
#     print('encuestado={}'.format(d.encuestado))
#     print('pregunta={}'.format(d.pregunta))
#     print('relacion={}'.format(d.relacion_pregunta))
#     if d.opcion_respuesta:
#         print('opcion{}, titulo={}'.format(d.opcion_respuesta, d.opcion_respuesta.titulo))
#     else:
#         print('opcion{}, titulo={}'.format(d.opcion_respuesta, d.opcion_respuesta))
#     print('detalle={}'.format(d.detalle_respuesta))

    
datos = DatosEncuestado.objects.filter(encuesta__slug="infantil")
nuevos_datos = []
for d in datos:
    respuestas_normalizado = {}
    for resp in d.respuesta.all():
        if resp.opcion_respuesta:
            print(resp.opcion_respuesta.titulo)
        # if resp.pregunta.id not in respuestas_normalizado:
        #     respuestas_normalizado[resp.pregunta.id] = []
            
        # respuestas_normalizado[resp.pregunta.id].append({
        #     'titulo': 'dasdasd'
        # })



    nuevos_datos.append({
        'encuesta': d.encuesta,
        'nombres': d.nombres,
        'apellidos': d.apellidos,
        'edad': d.edad,
        'genero': d.genero,
        'ciudad': d.ciudad,
        'email': d.email,
        'tiene_hijos': d.tiene_hijos,
        'edad_hijos': d.edad_hijos,
        'genero_hijo': d.genero_hijo,
        'respuestas': respuestas_normalizado
    })

print(nuevos_datos)


    
