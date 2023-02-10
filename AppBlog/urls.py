from django.urls import path, re_path
from .views import *
from .views import DetailMs, CanalDetailView, mensajes_privados, ListarUser,  Inbox
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'



urlpatterns = [
    
    path('', inicio, name="inicio"),
    path("leerTemas/", leerTemas, name="leerTemas"),
    path("leerTemas2/<id>", leerTemas2, name="leerTemas2"),
    path("agregarTema/", agregarTema, name="agregarTema"),
    path("editarTema/<id>", editarTema, name="editarTema"),
    path("eliminarTema/<id>", eliminarTema, name="eliminarTema"),
    path("buscar/", buscar, name="buscar"),
    path("temaBusq/", temaBusq, name="temaBusq"),

    path("register/", register, name="register"),
    path("login/", loginvista, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("verPerfil/", verPerfil, name="verPerfil"),
    path("acerca/", acerca, name="acerca"),
    path("ListarUser/", ListarUser, name="ListarUser"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("agregarImagen/", agregarImagen, name="agregarImagen"),
    path("agregarExtra/", agregarExtra, name="agregarExtra"),


    




    
    
    re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),
    path("dm/<str:username>", mensajes_privados),
    path("ms/<str:username>", DetailMs.as_view(), name="detailms"),
    path('Inbox', Inbox.as_view(), name="Inbox"),
    
    
    
]


