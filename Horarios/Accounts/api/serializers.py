from django.contrib.auth import get_user_model
from rest_framework import serializers
from CrearHorario.models import  Alumnos, Clases

User =  get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id'
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
    class Meta:
        model = Clases
        fields = [
            'IDClase',
            'Especialidad',
            'Materia',
            'Profesor'
        ]
