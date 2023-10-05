from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Curso, Profesores, Estudiantes, Entregable, Avatar, Inmueble, UserProfile
from datetime import datetime


class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada', 'fecha_creacion', 'antiguedad']
    search_fields = ['nombre', 'camada']
    list_filter = ['nombre',  'camada',]
    
    def antiguedad(self, object):
        print('*****',object)
        if object.fecha_creacion:
            return (datetime.now().date() - object.fecha_creacion).days

admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesores)
admin.site.register(Estudiantes)
admin.site.register(Entregable)
admin.site.register(Avatar)
admin.site.register(Inmueble)
admin.site.register(UserProfile)

