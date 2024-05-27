
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('listar/', views.listar_solicitudes, name='listar_solicitudes'),
    path('estadisticas/', views.estadisticas_solicitudes, name='estadisticas_solicitudes'),
]
