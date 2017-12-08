# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import FormUserNeededMixin

from .models import (Horario,
                     Alumnos)
from .forms import HorarioModelForm

from django.views.generic import    (ListView,
                                     CreateView,
                                     DeleteView,
                                     UpdateView,
                                     ListView)



# Create your views here.
    ##### Clases para borrar materia  contenido en un horario #####
class HorarioClaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Horario
    template_name = "crearhorarios/delete_confirm.html"
    success_url = reverse_lazy("horario_lista")

    ##### Clases para agregar materia en un horario #####
class HorarioMateriaCreateView(CreateView):
    form_class = HorarioModelForm
    template_name = "crearhorarios/agregar.html"
    success_url = reverse_lazy("horario_lista")


    ##### Clase para vizualizar el horario #####
class HorarioListView(ListView):
    template_name = "crearhorarios/horariosView_Ajax.html"

    def get_queryset(self, *args, **kwargs):
        qs = Horario.objects.all().order_by("-pk")
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(Alumno__Matricula__icontains=query)|
            Q(Alumno__user__id__icontains=query)|
            Q(Clase__IDClase__icontains=query)
            )
        return qs.filter(Alumno__user=self.request.user)

    def get_context_data(self, *args, **kwargs):
         context = super(HorarioListView, self).get_context_data(*args, **kwargs)
         print context
         context['create_form'] = HorarioModelForm()
         context['create_url'] = reverse_lazy("horario_lista")
         return context
