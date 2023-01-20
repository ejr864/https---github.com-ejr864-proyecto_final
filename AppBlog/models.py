from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Tema(models.Model):
    titulo= models.CharField(max_length=50)
    fecha= models.DateField(auto_now_add=True)
    autor= models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)
    contenido= models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.categoria} - {self.autor} - {self.contenido} "



class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars", null=True, blank = True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

