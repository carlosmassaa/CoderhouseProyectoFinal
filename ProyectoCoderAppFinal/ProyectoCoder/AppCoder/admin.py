from django.contrib import admin
from.models import Curso, Profesores, Estudiantes, Entregable, Avatar
from datetime import datetime

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada', 'fecha_creacion', 'antiguedad']
    search_fields = ['nombre', 'camada']
    list_filter = ['nombre',  'camada',]
    
    def antiguedad(self, object):
        print('*****',object)
        if object.fecha_creacion:
            return (datetime.now().date() - object.fecha_creacion).days


# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesores)
admin.site.register(Estudiantes)
admin.site.register(Entregable)
admin.site.register(Avatar)