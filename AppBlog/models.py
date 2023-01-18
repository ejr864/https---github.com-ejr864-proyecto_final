from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Tema(models.Model):
    titulo= models.CharField(max_length=50)
    fecha= models.DateField(default=datetime.now)
    autor= models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)
    contenido= models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.categoria} "


class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    usua= models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.usua} - {self.email}  "


class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars", null=True, blank = True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"