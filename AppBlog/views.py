from django.shortcuts import render

from django.http import HttpResponse, Http404

from django.urls import reverse_lazy

from .models import *      



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AppBlog.forms import TemaFormu,  RegistroUsuarioForm, UserEditForm, AvatarForm, ImagenTemaForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User


# Create your views here.

def inicio(request):

    return render (request, "AppBlog/inicio.html", {"avatar": obtenerAvatar(request)})


@login_required
def leerTemas(request):

    temas= Tema.objects.all()

    if temas!='':
        return render(request, "AppBlog/temario.html", {"temas": temas})
    else:
        return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje": "no hay tema vista"})




@login_required
def agregarTema(request):

    if request.method=="POST":

        form=TemaFormu(request.POST)

        if form.is_valid():

            info=form.cleaned_data

            titulo=info["titulo"]

            subtitulo=info["subtitulo"]

            autor=info["autor"]

            resumen=info["resumen"]    

            cuerpo=info["cuerpo"]    

            tema= Tema(titulo=titulo, subtitulo=subtitulo, autor=autor, resumen=resumen, cuerpo=cuerpo)

            tema.save()

            temas= Tema.objects.all()

            return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje": "tema guardado correctamente"})       
        else:

            return render(request, "AppBlog/temaFormulario.html", {"form": form, "mensaje": "informacion no valida"})
    else:

        form= TemaFormu()

        return render(request, "AppBlog/temaFormulario.html", {"form": form})



@login_required
def editarTema(request, id):
    tema= Tema.objects.get(id=id)
    if request.method=="POST":
        form=TemaFormu(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            tema.titulo=info["titulo"]
            tema.subtitulo=info["subtitulo"]
            tema.autor=info["autor"]  
            tema.resumen=info["resumen"]
            tema.cuerpo=info["cuerpo"]  
            tema.save()
            temas=Tema.objects.all()                        
            return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje":  "Tema editado correctamente"})
        pass
    else:        
        form= TemaFormu(initial={"titulo":tema.titulo, "subtitulo":tema.subtitulo, "autor":tema.autor, "resumen":tema.resumen, "cuerpo":tema.cuerpo})
        return render(request, "AppBlog/temaEdit.html", {"form": form, "tema": tema})



@login_required
def eliminarTema(request, id):

    tema= Tema.objects.get(id=id)
    tema.delete()

    temas= Tema.objects.all()

    return render(request, "AppBlog/temario.html", {"temas": temas, "mensaje": "tema eliminado correctamente"})      



def temaBusq(request):
    return render(request, "AppBlog/temaBusq.html")



@login_required
def buscar(request):
    titulo= request.GET["titulo"]
    if titulo!="":
        temas= Tema.objects.filter(titulo__contains =titulo)    
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
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppBlog/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBlog/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})


@login_required
def verPerfil(request):
    usuario=request.user
    return render(request, "AppBlog/verPerfil.html", {"usuario":usuario, "avatar": obtenerAvatar(request)})
	



@login_required
def leerTemas2(request, id):
    tema= Tema.objects.get(id=id)
    return render(request, "AppBlog/detalleTema.html", {"tema": tema})



def acerca(request):
    return render(request, "AppBlog/acerca.html")



@login_required
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user) 
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/avatarpordefecto.png"
    return avatar




def obtenerImagen(request):
    lista=Imagen.objects.filter(user=request.user) 
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        return render(request, {"mensaje": "imagen no guardada"})
    return imagen





def ListarUser(request):

    displayusername= User.objects.all()    
    return render(request, "AppBlog/verUsuarios.html", {"displayusername": displayusername})




def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user})



def agregarImagen(request):
    if request.method=="POST":
        form=ImagenTemaForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=Imagen(imagen=request.FILES["imagen"])
            imagenVieja=Imagen.objects.filter()
            if len(imagenVieja)>0:
                imagenVieja[0].delete()
            imagen.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"imagen agregado correctamente"})
        else:
            return render(request, "AppBlog/agregarImagen.html", {"form": form, "mensaje":"Error al agregar el imagen"})
    else:
        form=ImagenTemaForm()
        return render(request, "AppBlog/agregarImagen.html", {"form": form})





class CanalDetailView(LoginRequiredMixin, DetailView):
    template_name= "AppBlog/canal_detail.html"
    queryset = Canal.objects.all()
    



class DetailMs(LoginRequiredMixin, DetailView):

    template_name= "AppBlog/canal_detail.html" 
    def get_object(self, *args, **kwargs):

        username = self.kwargs.get("username")
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

        if username == mi_username:
            mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)
            return mi_canal


        if canal == None:
            raise Http404

        return canal


def mensajes_privados(request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")

    mi_username = request.user.username

    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("si, fue creado")

    Usuarios_Canal= canal.canalusuario_set.all().values("usuario__username")
    print(Usuarios_Canal)
    mensaje_canal = canal.canalmensaje_set.all()    
    print(mensaje_canal.values("texto"))

    return HttpResponse(f"Nuestro Id del Canal - {canal.id}")