from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    
class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='inmuebles/')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ciudad = models.CharField(max_length=100, default='Desconocida') 

    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.texto
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TIPOS_DE_USUARIO = (
        ('comprador', 'Comprador'),
        ('vendedor', 'Vendedor'),
    )
    tipo_de_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO)
    
    def __str__(self):
        return self.user.username
