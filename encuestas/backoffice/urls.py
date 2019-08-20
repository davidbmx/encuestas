from django.urls import path
from .views import dashboard, encuesta, export_xls

app_name = 'backoffice'

urlpatterns = [
    path('dashboard/', dashboard, name='backoffice'),
    path('encuesta/<int:id_encuesta>/', encuesta, name='list_encuesta'),
    path('encuesta/<int:id_encuesta>/exportar/', export_xls, name='exportar_encuesta'),
]
