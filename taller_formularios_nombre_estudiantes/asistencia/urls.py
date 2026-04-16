from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_asistencia, name='asistencia_registro'),
    path('confirmacion/', views.confirmacion_asistencia, name='asistencia_confirmacion'),
]
