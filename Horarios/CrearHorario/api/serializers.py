from rest_framework import serializers

from Accounts.api.serializers import UserDisplaySerializer, AlumnoDisplaySerializer, ClaseDisplaySerializer
from CrearHorario.models import  Horario

class HorarioModelSerializer(serializers.ModelSerializer):
    # user = UserDisplaySerializer(read_only=True)
    #Alumno = AlumnoDisplaySerializer()
    #Clase = ClaseDisplaySerializer()
    class Meta:
        model = Horario
        fields = [
            'id',
            'Alumno',
            'Clase'
        ]

    def get_alumno(self, obj):
        return obj.Alumno.strftime("%b %d %I:%M %p")
