# Generated by Django 5.1.2 on 2024-10-10 10:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('duracion_estimada', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('contrasenia', models.CharField(max_length=250, null=True)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Progreso', 'Progreso'), ('Completada', 'Completada')], max_length=20)),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateField()),
                ('hora_vencimiento', models.DateTimeField()),
                ('etiquetas_asociadas', models.ManyToManyField(to='GestionTareas.etiqueta')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='GestionTareas.proyecto')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas_creadas', to='GestionTareas.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos_creados', to='GestionTareas.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='proyectos_asignados', to='GestionTareas.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField()),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionTareas.tarea')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionTareas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionTareas.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionTareas.usuario')),
            ],
        ),
    ]