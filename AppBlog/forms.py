from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime


class TemaFormu(forms.Form):
    titulo= forms.CharField(label="Titulo Tema", max_length=50)
    categoria= forms.CharField(label="Categoria", max_length=50)
    contenido= forms.CharField(label="Contenido", max_length=50)

class RegistroUsuarioForm(UserCreationForm):
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
  