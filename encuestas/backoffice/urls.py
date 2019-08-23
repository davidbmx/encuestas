from django.urls import path
from .views import dashboard, encuesta, export_xls, encuestalist

app_name = 'backoffice'

urlpatterns = [
    path('dashboard/', dashboard, name='backoffice'),
    path('encuesta/<int:id_encuesta>/', encuesta, name='list_encuesta'),
    path('encuestalist/<int:id_encuesta>/', encuestalist, name='list_encuesta_list'),
    path('encuesta/<int:id_encuesta>/exportar/', export_xls, name='exportar_encuesta'),
]
