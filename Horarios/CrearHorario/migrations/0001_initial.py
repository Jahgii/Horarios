# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 03:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('Matricula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('Serie', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('IDClase', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Carreras')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Clases')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Alumnos')),
                ('Clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Clases')),
            ],
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('Clave', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('IDProfesor', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('IDTiempo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Tiempo', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='disponibilidad',
            name='Hora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Tiempo'),
        ),
        migrations.AddField(
            model_name='clases',
            name='Materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Materias'),
        ),
        migrations.AddField(
            model_name='clases',
            name='Profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Profesores'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='Carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrearHorario.Carreras'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]