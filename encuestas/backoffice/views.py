import xlwt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from encuestas.encuesta.models import Encuesta, DatosEncuestado, Pregunta
import json
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def dashboard(request):
    encuestas = Encuesta.objects.all()
    total = DatosEncuestado.objects.all().count()
    return render(request, 'backoffice/dashboard.html', {'encuestas': encuestas, 'total_encuestas': DatosEncuestado, 'total': total})

# @login_required
# def encuesta(request, id_encuesta):
#     encuesta = get_object_or_404(Encuesta, pk = id_encuesta)
#     encuestas = encuestas = Encuesta.objects.all()
#     # encuestado = DatosEncuestado.objects.filter(encuesta=encuesta)
#     preguntas = Pregunta.objects.filter(encuesta=encuesta)

#     datos = DatosEncuestado.objects.filter(encuesta=encuesta)
#     nuevos_datos = []
#     for d in datos:
#         respuestas_normalizado = {}
#         for resp in d.respuesta.all():
#             if resp.pregunta.id not in respuestas_normalizado:
#                 respuestas_normalizado[resp.pregunta.id] = []
#             titulo = ''
#             imagen = ''
#             if resp.opcion_respuesta:
#                 titulo = resp.opcion_respuesta.titulo
#                 if resp.opcion_respuesta.imagen:
#                     imagen = resp.opcion_respuesta.imagen.url

#             respuestas_normalizado[resp.pregunta.id].append({
#                 'titulo': titulo,
#                 'detalle': resp.detalle_respuesta,
#                 'pregunta': resp.pregunta, 
#                 'imagen': imagen
#             })

#         nuevos_datos.append({
#             'encuesta': d.encuesta,
#             'nombres': d.nombres,
#             'apellidos': d.apellidos,
#             'edad': d.edad,
#             'genero': d.genero,
#             'ciudad': d.ciudad,
#             'email': d.email,
#             'tiene_hijos': d.tiene_hijos,
#             'edad_hijos': d.edad_hijos,
#             'genero_hijo': d.genero_hijo,
#             'respuestas': respuestas_normalizado
#         })

#     context = {
#         'encuestas': encuestas,
#         'encuesta': encuesta,
#         'encuestado': nuevos_datos,
#         'preguntas': preguntas
#     }

#     return render(request, 'backoffice/encuesta.html', context)

@login_required
def encuesta(request, id_encuesta):
    encuesta = get_object_or_404(Encuesta, pk = id_encuesta)
    encuestas = encuestas = Encuesta.objects.all()
    preguntas = Pregunta.objects.filter(encuesta=encuesta)

    datos = DatosEncuestado.objects.filter(encuesta=encuesta)
    nuevos_datos = []
    for d in datos:
        respuestas_normalizado = {}
        for resp in d.respuesta.all():
            if resp.pregunta.id not in respuestas_normalizado:
                respuestas_normalizado[resp.pregunta.id] = []
            titulo = ''
            imagen = ''
            if resp.opcion_respuesta:
                titulo = resp.opcion_respuesta.titulo
                if resp.opcion_respuesta.imagen:
                    imagen = resp.opcion_respuesta.imagen.url

            respuestas_normalizado[resp.pregunta.id].append({
                'titulo': titulo,
                'detalle': resp.detalle_respuesta,
                'pregunta': resp.pregunta, 
                'imagen': imagen
            })

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

    context = {
        'encuestas': encuestas,
        'encuesta': encuesta,
        'encuestado': nuevos_datos,
        'preguntas': preguntas
    }

    return render(request, 'backoffice/encuesta.html', context)

# @login_required
# def encuestalist(request, id_encuesta):
#     encuesta = get_object_or_404(Encuesta, pk = id_encuesta)
#     encuestas = encuestas = Encuesta.objects.all()
#     preguntas = Pregunta.objects.filter(encuesta=encuesta)

#     data = DatosEncuestado.objects.filter(encuesta=encuesta)
#     page = request.GET.get('draw', 1)
#     paginator = Paginator(data, 10)
#     try:
#         datos = paginator.page(page)
#     except PageNotAnInteger:
#         datos = paginator.page(1)
#     except EmptyPage:
#         datos = paginator.page(paginator.num_pages)

#     nuevos_datos = []
#     for d in datos:
#         respuestas_normalizado = {}
#         for resp in d.respuesta.all():
#             if resp.pregunta.id not in respuestas_normalizado:
#                 respuestas_normalizado[resp.pregunta.id] = ''
#             titulo = ''
#             imagen = ''
#             if resp.opcion_respuesta:
#                 if resp.opcion_respuesta.titulo:
#                     titulo = 'Opcion: {}\n'.format(resp.opcion_respuesta.titulo)
#                 if resp.opcion_respuesta.imagen:
#                     imagen = resp.opcion_respuesta.imagen.url

#             # respuestas_normalizado[resp.pregunta.id].append({
#             #     'titulo': titulo,
#             #     'detalle': resp.detalle_respuesta,
#             #     'pregunta': resp.pregunta.id, 
#             #     'imagen': imagen
#             # })
#             detalle = ''
#             if resp.detalle_respuesta:
#                 detalle = 'Detalle: {} \n'.format(resp.detalle_respuesta)
#             respuestas_normalizado[resp.pregunta.id] += '{}{} {}'.format(titulo, detalle, imagen)
#                 # 'titulo': titulo,
#                 # 'detalle': resp.detalle_respuesta,
#                 # 'pregunta': resp.pregunta.id, 
#                 # 'imagen': imagen


#         nuevos_datos.append({
#             'encuesta': d.encuesta.nombre,
#             'nombres': d.nombres,
#             'apellidos': d.apellidos,
#             'edad': d.edad,
#             'genero': d.genero,
#             'ciudad': d.ciudad.nombre,
#             'email': d.email,
#             'tiene_hijos': d.tiene_hijos,
#             'edad_hijos': d.edad_hijos,
#             'genero_hijo': d.genero_hijo,
#             **respuestas_normalizado
#         })
#     response = {
#         "draw": page,
#         "recordsTotal": data.count(),
#         "recordsFiltered": data.count(),
#         'data': nuevos_datos
#     }
    
#     return HttpResponse(json.dumps(response), content_type='application/json')


@login_required
def export_xls(request, id_encuesta):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="encuesta.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Encuesta', cell_overwrite_ok=True)


    # section vars
    encuesta = get_object_or_404(Encuesta, pk = id_encuesta)
    preguntas = Pregunta.objects.filter(encuesta=encuesta)
    datos = DatosEncuestado.objects.filter(encuesta=encuesta)
    # end vars

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'Nombres',
        'Apellidos',
        'Edad',
        'Genero',
        'Ciudad',
        'tiene_hijos',
        'edad_hijos',
        'genero_hijo',
    ]

    for pregunta in preguntas:
        columns.append(pregunta.nombre)


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # vars data
    nuevos_datos = []
    for d in datos:
        respuestas_normalizado = {}
        for resp in d.respuesta.all():
            if resp.pregunta.id not in respuestas_normalizado:
                respuestas_normalizado[resp.pregunta.id] = []
            titulo = ''
            imagen = ''
            if resp.opcion_respuesta:
                titulo = resp.opcion_respuesta.titulo
                if resp.opcion_respuesta.imagen:
                    imagen = resp.opcion_respuesta.imagen.url

            respuestas_normalizado[resp.pregunta.id].append({
                'titulo': titulo,
                'detalle': resp.detalle_respuesta,
                'pregunta': resp.pregunta,
                'imagen': imagen
            })

        nuevos_datos.append({
            'encuesta': d.encuesta,
            'nombres': d.nombres,
            'apellidos': d.apellidos,
            'edad': d.edad,
            'genero': d.genero,
            'ciudad': d.ciudad.nombre,
            'email': d.email,
            'tiene_hijos': d.tiene_hijos,
            'edad_hijos': d.edad_hijos,
            'genero_hijo': d.genero_hijo,
            'respuestas': respuestas_normalizado
        })
    #end vars data

    
    for dato in nuevos_datos:
        row_num += 1
        tiene_hijos = 'NO'
        if dato['tiene_hijos']:
            tiene_hijos = 'SI'
        
        ws.write(row_num, 0, dato['nombres'], font_style)
        ws.write(row_num, 1, dato['apellidos'], font_style)
        ws.write(row_num, 2, dato['edad'], font_style)
        ws.write(row_num, 3, dato['genero'], font_style)
        ws.write(row_num, 4, dato['ciudad'], font_style)
        ws.write(row_num, 5, tiene_hijos, font_style)
        ws.write(row_num, 6, dato['edad_hijos'], font_style)
        ws.write(row_num, 7, dato['genero_hijo'], font_style)
        col_num = 7
        for key,value in dato['respuestas'].items():
            col_num += 1
            texto = []
            for i in value:
                if i['imagen']:
                    texto.append(i['imagen'].split('/')[-1])
                
                if i['titulo']:
                    texto.append('Opcion: {}'.format(i['titulo']))

                if i['detalle']:
                    texto.append('Detalle: {}'.format(i['detalle']))

            ws.write(row_num, col_num, '\n'.join(texto), font_style)

    wb.save(response)
    return response
