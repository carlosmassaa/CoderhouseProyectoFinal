from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views


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
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
    path('editar-avatar/', editar_avatar, name='EditarAvatar'),
    path('buscar/', buscar, name='Buscar'),    
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('editar-tipo-usuario/', views.editar_tipo_usuario, name='EditarTipoUsuario'),
    path('agregar-comentario/<int:id>/', agregar_comentario, name='AgregarComentario'),









    
    path('inmuebles/', views.inmuebles, name='Inmuebles'),
    path('inmuebles-formulario/', views.inmuebles_formulario, name='InmueblesFormulario'),
    path('lista-inmuebles/', views.listar_inmuebles, name='ListaInmuebles'),
    path('eliminar-inmueble/<int:id>', views.eliminar_inmueble, name='EliminarInmueble'),
    path('editar-inmueble/<int:id>', views.editar_inmueble, name='EditarInmueble'),
    path('detalle_inmueble/<int:id>/', views.detalle_inmueble, name='DetalleInmueble'),


]
