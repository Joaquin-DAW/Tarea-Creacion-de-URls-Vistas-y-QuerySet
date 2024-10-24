from django.shortcuts import render
from .models import Proyecto, Tarea, AsignacionTarea

# Create your views here.

def index(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'index.html', {'proyectos_mostrar': proyectos})

def listar_proyectos(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'proyecto/lista.html',{"proyectos_mostrar":proyectos})

def listar_tareas(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id) 
    tareas = Tarea.objects.filter(proyecto=proyecto).order_by('-fecha_creacion')
    
    return render(request, 'tarea/lista.html', {'proyecto': proyecto, 'tareas_mostrar': tareas})

def listar_usuarios_asignados(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id) 
    usuarios_asignados = AsignacionTarea.objects.filter(tarea=tarea).select_related('usuario').order_by('fecha_asignacion')

    return render(request, 'usuario/lista.html', {'tarea': tarea, 'usuarios_asignados': usuarios_asignados})