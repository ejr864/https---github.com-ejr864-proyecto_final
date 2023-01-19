from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicio, name="inicio"),
    path("leerTemas/", leerTemas, name="leerTemas"),
    path("agregarTema/", agregarTema, name="agregarTema"),
    path("editarTema/<id>", editarTema, name="editarTema"),
    path("eliminarTema/<id>", eliminarTema, name="eliminarTema"),
    path("buscar/", buscar, name="buscar"),
    path("temaBusq/", temaBusq, name="temaBusq"),
    
    
    
]