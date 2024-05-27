from django.shortcuts import render
from django.http import JsonResponse
from .models import Solicitud
from solicitudes_updated import models

def crear_solicitud(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        solicitud = Solicitud(nombre=nombre, descripcion=descripcion, estado=estado)
        solicitud.save()
        return JsonResponse({'mensaje': 'Solicitud creada exitosamente'}, status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    data = [{'id': s.id, 'nombre': s.nombre, 'descripcion': s.descripcion, 'fecha_solicitud': s.fecha_solicitud, 'estado': s.estado} for s in solicitudes]
    return JsonResponse({'solicitudes': data}, status=200)

def estadisticas_solicitudes(request):
    total = Solicitud.objects.count()
    estados = Solicitud.objects.values('estado').annotate(count=models.Count('estado'))
    estadisticas = {'total': total, 'estados': list(estados)}
    solicitudes = Solicitud.objects.all()
    return render(request, 'indexSolicitudes.html', {'estadisticas': estadisticas, 'solicitudes': solicitudes})

