from django import forms
from .models import Profesores, Estudiantes, Curso, Avatar, Inmueble, UserProfile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import User  


class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'camada')
    
class ProfesoresFormulario(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre', 'apellido', 'email', 'profesion', 'cursos']
        widgets = {
            'cursos': forms.CheckboxSelectMultiple
        }

class EstudiantesFormulario(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'email']


class UserEditForm(UserChangeForm):
    
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ('email', 'first_name', 'last_name', 'password1','password2') 
        
    def clean_password2(self):
        cleaned_data = super().clean()  # Llama al método clean() de la clase base
        password1 = cleaned_data["password1"]
        password2 = cleaned_data["password2"]
        
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")        
        return password2


class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ("imagen", )
        

class InmuebleFormulario(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'ubicacion', 'descripcion', 'foto', 'precio', 'ciudad']

        
        


class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['tipo_de_usuario']
        
        
        



