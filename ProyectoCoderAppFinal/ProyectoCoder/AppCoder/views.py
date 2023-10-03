from django.shortcuts import render
from .models import Curso, Profesores, Estudiantes, Avatar
from django.http import HttpResponse, HttpRequest
from .forms import CursoFormulario, ProfesoresFormulario, EstudiantesFormulario, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def curso (req, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f""" <P> Curso: {curso.nombre} - Camada: {curso.camada} creado con éxito!<P>""")

def listar_cursos(req):

    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos":lista})

def inicio(req):
    
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, 'inicio.html', {"url_avatar": avatar.imagen.url})
    except:
        return render(req, 'inicio.html')

def cursos(req):
    return render(req, 'cursos.html')
    return HttpResponse("Vista de Cursos")


def cursoFormulario(req):
    
    print('method', req.method)
    print('method', req.POST)
    if req.method == 'POST':
        
        miFormulario = CursoFormulario(req.POST)
    
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            return render(req, "inicio.html")
        
    else:
        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(req):
    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):
    
    if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(req, "resultadosBusqueda.html", {'cursos': cursos})

    else: 
        return HttpResponse(f"Debe agregar una camada")
        
        

def profesores(req):
    return render(req, 'profesores.html')
    return HttpResponse("Vista de Profesores")


from .forms import ProfesoresFormulario

def profesoresFormulario(req):
    if req.method == 'POST':
        miFormulario = ProfesoresFormulario(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "inicio.html")
    else:
        miFormulario = ProfesoresFormulario()
    return render(req, "profesoresFormulario.html", {"miFormulario": miFormulario})

@staff_member_required(login_url='/app-coder/login')
def listar_profesores(req):

    lista = Profesores.objects.all()
    
    return render(req, "lista_profesores.html", {"lista_profesores":lista})


def eliminar_profesor(req, id):
    
    if req.method == 'POST':
        
        profesores = Profesores.objects.get(id=id)
        profesores.delete()
        
        profesores = Profesores.objects.all()
        
        return render(req, "lista_profesores.html", {"profesores": profesores})
    
def editar_profesor(req, id):     
    profesores = Profesores.objects.get(id=id)
    if req.method == 'POST':
        miFormulario = ProfesoresFormulario(req.POST) 
        if miFormulario.is_valid():
                
                data = miFormulario.cleaned_data
                profesores.nombre = data["nombre"]
                profesores.apellido = data["apellido"]
                profesores.email = data["email"]
                profesores.profesion = data["profesion"]
                profesores.save()
                
                return render(req, "inicio.html")
    else:
        
         miFormulario = ProfesoresFormulario(initial={
        "nombre": profesores.nombre,
        "apellido": profesores.apellido,                                                
        "email": profesores.email,                                              
        "profesion": profesores.profesion,
         })
         return render(req, "editarProfesor.html", {"miFormulario": miFormulario, "id":profesores.id})
         



def estudiantes(req):
    return render(req, 'estudiantes.html')
    return HttpResponse("Vista de Estudiantes")

def listar_estudiantes(req):

    lista = Estudiantes.objects.all()
    
    return render(req, "lista_estudiantes.html", {"lista_estudiante":lista})

def estudiantesFormulario(req):
    if req.method == 'POST':
        miFormulario = EstudiantesFormulario(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "inicio.html")
    else:
        miFormulario = EstudiantesFormulario()
    return render(req, "estudiantesFormulario.html", {"miFormulario": miFormulario})


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"


class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"


class CursoCreate(CreateView):
    model = Curso
    Create = "curso_create.html"
    context_object_name = "curso"
    fields = ['nombre', 'camada']
    success_url = '/app-coder/lista-cursos'
    

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    form_class = CursoFormulario
    success_url = '/app-coder/listaCursos'
    context_object_name = "curso"
    

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = '/app-coder/lista-cursos'
    
    
def entregables(req):
    return render(req, 'entregables.html')  
    return HttpResponse("Vista de Entregables")

def loginView(req):
    
    
    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST) 
        if miFormulario.is_valid():
                
                data = miFormulario.cleaned_data
                usuario = data["username"]
                psw = data["password"]
                
                user = authenticate(username=usuario, password=psw)
                if user:
                    login(req, user)
                    return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})                   
    else:
        
         miFormulario = AuthenticationForm()
         return render(req, "login.html", {"miFormulario": miFormulario})
     
def register(req):     
    if req.method == 'POST':
        miFormulario = UserCreationForm(req.POST) 
        if miFormulario.is_valid():
                
                data = miFormulario.cleaned_data
                usuario = data["username"]
                miFormulario.save()                
                return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})                
                    
                                
        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})    
                   
    else:
        
         miFormulario = UserCreationForm()
         return render(req, "registro.html", {"miFormulario": miFormulario})    
     
def editar_perfil(req):
    usuario = req.user
    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user) 
        if miFormulario.is_valid():
                
                
                data = miFormulario.cleaned_data
                usuario.first_name = data["first_name"]
                usuario.last_name = data["last_name"]
                usuario.email = data["email"]
                usuario.set_password(data["password1"])
                usuario.save()
                
                return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:    
            return render(req, "editarperfil.html", {"miFormulario": miFormulario})
    else:
        
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarperfil.html", {"miFormulario": miFormulario})

def agregar_avatar(req)    :
    
    if req.method == 'POST':
        
        miFormulario = AvatarFormulario(req.POST, req.FILES) 
        
        if miFormulario.is_valid():
                
                
                data = miFormulario.cleaned_data
                avatar = Avatar(user=req.user, imagen=data["imagen"])
                avatar.save()
                
                return render(req, "inicio.html", {"mensaje": "Avatar actualizado con éxito!"})
        else:    
            return render(req, "editarperfil.html", {"miFormulario": miFormulario})
    else:
        
        miFormulario = AvatarFormulario(instance=avatar)
        return render(req, "agregarAvatar.html", {"miFormulario": miFormulario})
