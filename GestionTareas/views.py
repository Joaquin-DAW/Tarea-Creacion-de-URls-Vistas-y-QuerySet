from django.shortcuts import render
from .models import Proyecto, Tarea, AsignacionTarea, Comentario, Etiqueta, Usuario
from django.views.defaults import page_not_found

# Create your views here.

def index(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'index.html', {'proyectos_mostrar': proyectos})

def listar_proyectos(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'proyecto/lista.html',{"proyectos_mostrar":proyectos})

def listar_tareas_asignadas(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id) 
    tareas = Tarea.objects.filter(proyecto=proyecto).order_by('-fecha_creacion')
    
    return render(request, 'tarea/lista.html', {'proyecto': proyecto, 'tareas_mostrar': tareas})

def listar_usuarios_asignados(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id) 
    usuarios_asignados = AsignacionTarea.objects.filter(tarea=tarea).select_related('usuario').order_by('fecha_asignacion')

    return render(request, 'usuario/lista.html', {'tarea': tarea, 'usuarios_asignados': usuarios_asignados})

def listar_tareas_texto(request, texto):
    asignaciones = AsignacionTarea.objects.filter(observaciones__contains=texto).order_by('-fecha_asignacion')
    tareas = set(asignacion.tarea for asignacion in asignaciones)
    
    return render(request, 'tarea/lista_observaciones.html', {'tareas_mostrar': tareas, 'texto_buscado': texto, 'asignaciones': asignaciones})

def listar_tareas_completadas(request, anio_inicio, anio_fin):
    tareas_completadas = Tarea.objects.filter(estado='Completada', fecha_creacion__year__gte=anio_inicio, 
                                              fecha_creacion__year__lte=anio_fin).order_by('-fecha_creacion')

    return render(request, 'tarea/lista_completadas.html', {'tareas_mostrar': tareas_completadas, 'anio_inicio': anio_inicio, 'anio_fin': anio_fin})

def ultimo_comentario_usuario(request, proyecto_id, tarea_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    tarea = Tarea.objects.get(id=tarea_id, proyecto=proyecto)
    ultimo_comentario = Comentario.objects.filter(tarea=tarea).order_by('-fecha_comentario').first()

    return render(request, 'usuario/ultimo_comentario.html', {'tarea': tarea, 'ultimo_comentario': ultimo_comentario})

def comentarios_tarea_concreta(request, tarea_id, palabra, anio):
    tarea = Tarea.objects.get(id=tarea_id)
    comentarios = Comentario.objects.filter(tarea=tarea, contenido__startswith=palabra, fecha_comentario__year=anio)

    return render(request, 'tarea/comentarios_tarea.html', {'tarea': tarea,'comentarios': comentarios,'palabra': palabra,'anio': anio})

def listar_etiquetas_tareas_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    etiquetas = Etiqueta.objects.filter(tarea__in=tareas).distinct()

    return render(request, 'proyecto/lista_etiquetas_proyecto.html', {'proyecto': proyecto, 'etiquetas': etiquetas})

def listar_usuarios_no_asignados(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    usuarios_asignados = Usuario.objects.filter(asignaciontarea__tarea=tarea)
    usuarios_no_asignados = Usuario.objects.exclude(id__in=usuarios_asignados)

    return render(request, 'usuario/usuarios_no_asignados.html', {'tarea': tarea, 'usuarios_no_asignados': usuarios_no_asignados})

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errors/400.html', None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errors/403.html', None,None,403)

def mi_error_500(request):
    return render(request, 'errors/500.html', None,None,500)