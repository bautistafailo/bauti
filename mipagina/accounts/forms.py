from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario de registro de usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo')  # Campo de correo electrónico
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  # Campo de contraseña
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)  # Campo de confirmación de contraseña

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # Campos del formulario
        help_texts = {key: '' for key in fields}  # Desactivar mensajes de ayuda predeterminados


# Formulario de edición de usuario
class EditarUsuarioForm(forms.Form):
    email = forms.EmailField(required=False)  # Campo de correo electrónico 
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)  # Campo de nombre 
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)  # Campo de apellido 
    avatar = forms.ImageField(required=False)  # Campo de imagen de avatar 






