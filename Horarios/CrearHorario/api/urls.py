from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import HorarioListAPIView, HorarioCreateAPIView

urlpatterns=[
    url(r'^$', HorarioListAPIView.as_view(), name = 'list'),
    url(r'^create/$', HorarioCreateAPIView.as_view(), name='create'),
]
