from django.urls import path
from .views import encuesta

urlpatterns = [
    path('encuesta/', encuesta, name='encuesta'),
]
