from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='lista_proyectos'),
    path('tareas/<int:proyecto_id>', views.listar_tareas, name='lista_tarea_asignada'),
    path('tareas/<int:tarea_id>/usuario', views.listar_usuarios_asignados, name='lista_usuarios_asignados'),
]