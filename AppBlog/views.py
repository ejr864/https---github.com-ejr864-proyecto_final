from django.shortcuts import render

from django.http import HttpResponse

from .models import *

from AppBlog.forms import TemaFormu,  RegistroUsuarioForm, UserEditForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.

def inicio(request):

    return render (request, "AppBlog/inicio.html")



def leerTemas(request):

    temas= Tema.objects.all()

    return render(request, "AppBlog/temario.html", {"temas": temas})



def agregarTema(request):

    if request.method=="POST":

        form=TemaFormu(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            titulo=info["titulo"]

            autor=info["autor"]

            categoria=info["categoria"]

            contenido=info["contenido"]    

            tema= Tema(titulo=titulo, autor=autor, categoria=categoria, contenido=contenido)

            tema.save()

            temas= Tema.objects.all()

            return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje": "tema guardado correctamente"})       
        else:

            return render(request, "AppBlog/temaFormulario.html", {"form": form, "mensaje": "info no valida"})
    else:

        form= TemaFormu()

        return render(request, "AppBlog/temaFormulario.html", {"form": form, "mensaje": "info no valida"})




def editarTema(request, id):

    tema= Tema.objects.get(id=id)

    if request.method=="POST":

        form=TemaFormu(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            tema.titulo=info["titulo"]

            tema.autor=info["autor"]  

            tema.categoria=info["categoria"]

            tema.contenido=info["contenido"]  

            tema.save()

            temas=Tema.objects.all()                         

            return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje":  "Tema editado correctamente"})
        pass
    else:        

        form= TemaFormu(initial={"titulo":tema.titulo, "autor":tema.autor, "categoria":tema.categoria, "contenido":tema.contenido})

        return render(request, "AppBlog/temaEdit.html", {"form": form, "tema": tema})




def eliminarTema(request, id):

    tema= Tema.objects.get(id=id)
    tema.delete()

    temas= Tema.objects.all()

    return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje": "tema eliminado correctamente"})      



def temaBusq(request):
    return render(request, "AppBlog/temaBusq.html")




def buscar(request):
    titulo= request.GET["titulo"]
    if titulo!="":
        temas= Tema.objects.filter(titulo=titulo)       
        return render(request, "AppBlog/temaBusqResul.html", {"temas": temas})
    else:
        return render(request, "AppBlog/temaBusq.html", {"mensaje": "ingresa un titulo existente"})  








def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppBlog/inicio.html" ,{"mensaje":f"Usuario {username} creado correctamente"})    
        else:
            return render(request, "AppBlog/register.html", {"form": form, "mensaje": "Error al crear usuario"})
    else: 
        form= RegistroUsuarioForm()
        return render(request, "AppBlog/register.html", {"form": form})






def loginvista(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usu} logeado correctamente"})
            else:
                return render(request, "AppBlog/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrecto"})
        else: 
            return render(request, "AppBlog/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrecto"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlog/login.html", {"form":form})



def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

        




