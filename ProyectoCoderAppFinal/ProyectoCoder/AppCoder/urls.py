from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('login/', loginView, name='Login'),
    path('register/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
    path('editar-avatar/', editar_avatar, name='EditarAvatar'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('editar-tipo-usuario/', views.editar_tipo_usuario, name='EditarTipoUsuario'),
    path('agregar-comentario/<int:id>/', agregar_comentario, name='AgregarComentario'),
    path('acercademi/', views.acerca_de_mi, name='AcercaDeMi'),
    path('inmuebles/', views.inmuebles, name='Inmuebles'),
    path('inmuebles-formulario/', views.inmuebles_formulario, name='InmueblesFormulario'),
    path('lista-inmuebles/', views.listar_inmuebles, name='ListaInmuebles'),
    path('eliminar-inmueble/<int:id>', views.eliminar_inmueble, name='EliminarInmueble'),
    path('editar-inmueble/<int:id>', views.editar_inmueble, name='EditarInmueble'),
    path('detalle_inmueble/<int:id>/', views.detalle_inmueble, name='DetalleInmueble'),
    path('links/', views.mostrar_links, name='links'),

]
