from django.test import TestCase
from .models import CanalMensaje, CanalUsuario, Canal
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your tests here.
class CanalTestCase(TestCase):
    def setUp(self):
        self.usuario_a = User.objects.create(username='juan', password='1234')
        self.usuario_a = User.objects.create(username='jose', password='4321')
        self.usuario_a = User.objects.create(username='joha', password='12345')


    def test_usuario_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 3)

    
    def test_cada_usuario_canal(self):
        qs = User.objects.all()
        for usuario in qs:
            canal_obj = Canal.objects.create()
            canal_obj.usuarios.add(usuario)

        canal_qs = Canal.objects.all()
        self.assertEqual(canal_qs.count(), 3)

        canal_qs_1 = canal_qs.solo_uno()
        self.assertEqual(canal_qs_1.count(), canal_qs.count())
    
    def prueba_dos_usuarios(self):
        canal_obj = Canal.objects.create()
        CanalUsuario.objects.create(usuario=self.jose, canal=canal_obj)
        CanalUsuario.objects.create(usuario=self.joha, canal=canal_obj)
        
        canal_obj2 = Canal.objects.create()
        CanalUsuario.objects.create(usuario=self.juan, canal=canal_obj2)

        qs = User.objects.all()
        self.assertEqual(qs.count(), 2)

        solo_dos = qs.solo_dos()
        self.assertEqual(solo_dos.count(), 1)
        
        


