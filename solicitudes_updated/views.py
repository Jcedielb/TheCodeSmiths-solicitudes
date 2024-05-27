
from django.shortcuts import render
from django.http import JsonResponse
from .models import Solicitud

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
    data = [{'nombre': s.nombre, 'descripcion': s.descripcion, 'fecha_solicitud': s.fecha_solicitud, 'estado': s.estado} for s in solicitudes]
    return JsonResponse({'solicitudes': data}, status=200)

def estadisticas_solicitudes(request):
    total = Solicitud.objects.count()
    estados = Solicitud.objects.values('estado').annotate(count=models.Count('estado'))
    data = {'total': total, 'estados': list(estados)}
    return JsonResponse({'estadisticas': data}, status=200)
