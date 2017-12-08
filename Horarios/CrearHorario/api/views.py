from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from CrearHorario.models import Horario
from .pagination import StandardResultPagination
from .serializers import HorarioModelSerializer

class HorarioCreateAPIView(generics.CreateAPIView):
    serializer_class = HorarioModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HorarioListAPIView(generics.ListAPIView):
    serializer_class = HorarioModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Horario.objects.all().order_by("-Alumno")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(Alumno__Matricula__icontains=query)|
                            Q(Clase__IDClase__icontains=query)
                          )
        return qs
