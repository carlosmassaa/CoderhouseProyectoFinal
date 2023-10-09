from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import User, UserProfile
from .models import Avatar, Inmueble, UserProfile


class UserEditForm(UserChangeForm):
    
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2') 
        
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
