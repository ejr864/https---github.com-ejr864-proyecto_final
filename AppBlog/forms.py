from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ModelForm, Textarea
from .models import Tema 



class TemaFormu(forms.Form):
    titulo= forms.CharField(label="Titulo Tema", max_length=50)
    subtitulo= forms.CharField(label="Subtitulo", max_length=50)
    autor= forms.CharField(label="Autor", max_length=50)
    resumen= forms.CharField(label="Resumen", max_length=50)
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.Textarea)



  

class RegistroUsuarioForm(UserCreationForm):
    username= forms.CharField(label="Nombre de Usuario")
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    

    class Meta:
        model= User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}
  


class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")

    class Meta:
        model= User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
  

class ImagenTemaForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")