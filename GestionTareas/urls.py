from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyectos/listar',views.listar_proyectos,name='lista_proyectos'),
    path('tareas/<int:proyecto_id>', views.listar_tareas_asignadas, name='lista_tarea_asignada'),
    path('tareas/<int:tarea_id>/usuario', views.listar_usuarios_asignados, name='lista_usuarios_asignados'),
    path('tareas/observaciones/<str:texto>', views.listar_tareas_texto, name='lista_tarea_texto'),
    path('tareas/completadas/<int:anio_inicio>/<int:anio_fin>/', views.listar_tareas_completadas, name='lista_tareas_completadas'),
    path('proyecto/<int:proyecto_id>/tarea/<int:tarea_id>/ultimo_comentario/', views.ultimo_comentario_usuario, name='ultimo_comentario_usuario'),
    path('tarea/<int:tarea_id>/comentarios/<str:palabra>/<int:anio>/', views.comentarios_tarea_concreta, name='comentarios_tarea'),
    path('proyecto/<int:proyecto_id>/etiquetas/', views.listar_etiquetas_tareas_proyecto, name='lista_etiquetas_tareas_proyecto'),
    path('tarea/<int:tarea_id>/usuarios/no_asignados/', views.listar_usuarios_no_asignados, name='lista_usuarios_no_asignados'),
]