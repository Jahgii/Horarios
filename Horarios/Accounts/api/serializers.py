from django.contrib.auth import get_user_model
from rest_framework import serializers
from CrearHorario.models import  Alumnos, Clases, Materias, Profesores

User =  get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id'
        ]

class MateriasDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = [
            'Clave',
            'Nombre'
        ]

class ProfesoresDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = [
            'IDProfesor',
            'Nombres',
            'Apellidos',
            'Correo'
        ]

class AlumnoDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = [
            'user',
            'Matricula',
            'Carrera',
            'Nombres',
            'Apellidos',
            'Correo'
        ]

class ClaseDisplaySerializer(serializers.ModelSerializer):
    Materia = MateriasDisplaySerializer(read_only=True)
    Profesor = ProfesoresDisplaySerializer(read_only=True)
    class Meta:
        model = Clases
        fields = [
            'IDClase',
            'Especialidad',
            'Materia',
            'Profesor'
        ]
