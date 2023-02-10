from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.db.models import Count
from django.db import models
from django.apps import apps
import uuid


User = settings.AUTH_USER_MODEL

# Create your models here.

# Modelo Tema
class Tema(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    fecha= models.DateField(auto_now_add=True)
    autor= models.CharField(max_length=50)
    resumen= models.CharField(max_length=50)
    cuerpo= models.CharField(max_length=200)
    img_tema= models.ImageField(null=True, blank=True, upload_to="img")
    

    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} - {self.fecha} - {self.resumen} - {self.autor} - {self.cuerpo} "

#modelo Avatar
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars", null=True, blank = True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"



class Extra(models.Model):
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    pagina = models.URLField(max_length = 200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.user} - {self.direccion} - {self.telefono} - {self.pagina} - {self.user}"




#Modelo displayusername sirve para mostrar nombre de usuario


class ModelBase(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
	tiempo = models.DateTimeField(auto_now_add=True)
	actualizar = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class CanalMensaje(ModelBase):
	canal   = models.ForeignKey("Canal", on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	texto =  models.TextField()

class CanalUsuario(ModelBase):
	canal  = models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class CanalQuerySet(models.QuerySet):

	def solo_uno(self):
		return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

	def solo_dos(self):
		return self.annotate(num_usuarios= Count("usuarios")).filter(num_usuarios=2)

	def filtrar_por_username(self, username):
		return self.filter(canalusuario__usuario__username=username)


class CanalManager(models.Manager):
	
	def get_queryset(self, *args, **kwargs):
		return CanalQuerySet(self.model, using=self._db)

	def filtrar_ms_por_privado(self, username_a, username_b):
		return self.get_queryset().solo_dos().filtrar_por_username(username_a).filtrar_por_username(username_b)

	def obtener_o_crear_canal_usuario_actual(self, user):
		qs = self.get_queryset().solo_uno().filtrar_por_username(user.username)
		if qs.exists():
			return qs.order_by("tiempo").first, False

		canal_obj = Canal.objects.create()
		CanalUsuario.objects.create(usuario=user, canal=canal_obj)
		return canal_obj, True

	def obtener_o_crear_canal_ms(self, username_a, username_b):
		qs = self.filtrar_ms_por_privado(username_a, username_b)
		if qs.exists():

			return qs.order_by("tiempo").first(), False #obj, created

		User = apps.get_model("auth", model_name='User')
		usuario_a, usuario_b = None, None
		try:
			usuario_a = User.objects.get(username=username_a)
		except User.DoesNotExist:
			return None, False

		try:
			usuario_b = User.objects.get(username=username_b)
		except User.DoesNotExist:
			return None, False

		if usuario_a == None or usuario_b==None:
			return None, False

		
		obj_canal =Canal.objects.create()
		canal_usuario_a = CanalUsuario(usuario=usuario_a, canal=obj_canal)
		canal_usuario_b = CanalUsuario(usuario=usuario_b, canal=obj_canal)
		CanalUsuario.objects.bulk_create([canal_usuario_a, canal_usuario_b])
		return obj_canal, True

class Canal(ModelBase):


	usuarios = models.ManyToManyField(User, blank=True, through=CanalUsuario)

	objects = CanalManager()

class displayusername(models.Model):
    username= models.CharField(max_length=50)