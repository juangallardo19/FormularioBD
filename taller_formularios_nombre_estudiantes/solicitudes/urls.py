from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_solicitud, name='solicitud_registro'),
    path('confirmacion/', views.confirmacion_solicitud, name='solicitud_confirmacion'),
]
