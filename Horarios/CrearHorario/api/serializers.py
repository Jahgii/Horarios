from rest_framework import serializers

from Accounts.api.serializers import UserDisplaySerializer, AlumnoDisplaySerializer, ClaseDisplaySerializer
from CrearHorario.models import  Horario

class HorarioModelSerializer(serializers.ModelSerializer):
    # user = UserDisplaySerializer(read_only=True)
    Alumno = AlumnoDisplaySerializer(read_only=True)
    Clase = ClaseDisplaySerializer(read_only=True)
    class Meta:
        model = Horario
        fields = [
            'Alumno',
            'Clase'
        ]
