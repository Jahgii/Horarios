# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Carreras, Alumnos, Materias, Profesores, Clases, Tiempo, Disponibilidad, Horario

# Register your models here.

admin.site.register(Carreras)
admin.site.register(Alumnos)
admin.site.register(Materias)
admin.site.register(Profesores)
admin.site.register(Clases)
admin.site.register(Tiempo)
admin.site.register(Disponibilidad)
admin.site.register(Horario)
