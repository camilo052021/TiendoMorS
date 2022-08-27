from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=50, default='Ciudad')
    direccion = models.CharField(max_length=100, default='Dirección')
    telefono = models.CharField(max_length=10, default='Teléfono')
    
    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'



   