from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name='ListaCursos'),
    path('lista-profesores/', listar_profesores, name='ListaProfesores'),
    path('lista-estudiantes/', listar_estudiantes, name='ListaEstudiante'),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-Formulario/', cursoFormulario, name='CursoFormulario'),
    path('profesores-Formulario/', profesoresFormulario, name='ProfesoresFormulario'),
    path('estudiantes-Formulario/', estudiantesFormulario, name='EstudiantesFormulario'),
    path('busqueda-Camada/', busquedaCamada, name='BusquedaCamada'),
    path('eliminarPorfesor/<int:id>', eliminar_profesor, name='EliminarProfesores'),
    path('editarProfesor/<int:id>', editar_profesor, name='EditarProfesor'),
    path('listaCursos/', CursoList.as_view(), name='ListarCursos'),
    path('detalleCurso/<pk>', CursoDetail.as_view(), name='DetalleCurso'),
    path('creaCurso/', CursoCreate.as_view(), name='CreaCurso'),
    path('actualizarCurso/<pk>', CursoUpdate.as_view(), name='ActualizarCurso'),
    path('eliminarCurso/<pk>', CursoDelete.as_view(), name='EliminarCurso'),
    path('login/', loginView, name='Login'),
    path('register/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
    path('buscar/', buscar, name='Buscar'),    
]
