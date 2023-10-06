from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}-{self.camada}'
    
    class Meta():
    
        verbose_name = 'Course'
        verbose_name_plural = 'The_Courses'
        ordering = ('nombre','-camada')
        unique_together = ('nombre','camada')
    
class Estudiantes(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
class Profesores(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()  
    profesion = models.CharField(max_length=50)  
    cursos = models.ManyToManyField(Curso)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link= models.CharField(max_length=256, null=True)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)

    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    
class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='inmuebles/')
    comentarios = models.ManyToManyField(User, through='Comentario')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Establece 0 como valor predeterminado
    ciudad = models.CharField(max_length=100, default='Desconocida') 

    def __str__(self):
        return self.nombre




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
        ('admin', 'Admin'),
    )
    tipo_de_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO)

    def __str__(self):
        return self.user.username
    


