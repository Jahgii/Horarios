#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Carreras(models.Model):   # Migracion 0001
    Serie   = models.CharField(primary_key=True, max_length=5)
    Nombre  = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

class Alumnos(models.Model):   # Migracion 0001
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    Matricula   = models.CharField(primary_key=True, max_length=8)
    Carrera     = models.ForeignKey(Carreras)
    Nombres     = models.CharField(max_length=50)
    Apellidos   = models.CharField(max_length=50)
    Correo      = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.Matricula)+ " " + str(self.Nombres)+ " " + str(self.Apellidos)

class Materias(models.Model):   # Migracion 0001
    Clave   = models.CharField(primary_key=True, max_length=8)
    Nombre  = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

class Profesores(models.Model):   # Migracion 0001
    IDProfesor  = models.CharField(primary_key=True, max_length=8)
    Nombres     = models.CharField(max_length=50)
    Apellidos   = models.CharField(max_length=50)
    Correo      = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.Nombres )+ " " + str(self.Apellidos)

class Clases(models.Model):   # Migracion 0001
    IDClase         = models.CharField(primary_key=True, max_length=4)
    Especialidad    = models.ForeignKey(Carreras)
    Materia         = models.ForeignKey(Materias)
    Profesor        = models.ForeignKey(Profesores)

    def __str__(self):
        return str(self.IDClase)

class Tiempo(models.Model):   # Migracion 0001
    IDTiempo    = models.CharField(primary_key=True, max_length=8)
    Tiempo      = models.TimeField();

    def __str__(self):
        return str(self.IDTiempo)

class Disponibilidad(models.Model):   # Migracion 0001
    Clase   = models.ForeignKey(Clases)
    Hora    = models.ForeignKey(Tiempo)

class Horario(models.Model):   # Migracion 0001
    Alumno  = models.ForeignKey(Alumnos)
    Clase   = models.ForeignKey(Clases)
