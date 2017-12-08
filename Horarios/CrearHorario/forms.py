from django import forms
from django.contrib.admin import widgets
from .models import Horario

class HorarioModelForm(forms.ModelForm):

    class Meta:
        model = Horario
        fields = [
            #"user",
            "Alumno",
            "Clase"
            ]
