from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBlog.forms import TemaFormu

# Create your views here.
def inicio(request):
    return render (request, "AppBlog/inicio.html")


def leerTemas(request):
    temas= Tema.objects.all()
    return render(request, "AppBlog/temario.html", {"temas": temas})
    

def agregarTema(request):
    if request.method=="POST":
        pass
    else:
        form= TemaFormu()
        return render(request, "AppBlog/temaFormulario.html", {"form": form, "mensaje": "info no valida"})



    # def profeFormulario(request):
    # if request.method=="POST":
    #     formulario= ProfeFormu(request.POST)
    #     if formulario.is_valid():
    #         info=formulario.cleaned_data
    #         nombre= info["nombre"]
    #         apellido= info["apellido"]
    #         email= info["email"]
    #         profesion= info["profesion"]
    #         profesor= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    #         profesor.save()
    #         profesores=Profesor.objects.all()
    #         return render(request, "AppCoder/profesores.html" ,{ "profesores":profesores,"mensaje": "Profesor guardado correctamente"})
    #     else:
    #         return render(request, "AppCoder/profeFormulario.html" ,{"formulario": formulario, "mensaje": "Informacion no valida"})
    # else:
    #     formulario= ProfeFormu()
    #     return render (request, "AppCoder/profeFormulario.html", {"formulario": formulario})
