from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from accounts import forms
from accounts import models
from django.forms.fields import EmailField, CharField, ImageField
from django import forms

def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/crear_account.html', {'formulario': form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'accounts/crear_account.html', {'formulario': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, "accounts/iniciar_sesion.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/iniciar_sesion.html', {'formulario': form})


@login_required
def mostrar_perfil(request):
    return render(request, 'accounts/mostrar_account.html')


class Logout(LogoutView):
    template_name = 'accounts/logout_account.html'


class EditarUsuarioForm(UserChangeForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']


class EditarAvatarForm(forms.ModelForm):
    class Meta:
        model = models.Accounts3
        fields = ['avatar']


@login_required
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ = models.Accounts3.objects.get_or_create(user=usuario)
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, request.FILES, instance=usuario)
        avatar_form = EditarAvatarForm(request.POST, request.FILES, instance=modelo_perfil)
        
        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_form.save()
            return redirect('index')
    else:
        form = EditarUsuarioForm(instance=usuario)
        avatar_form = EditarAvatarForm(instance=modelo_perfil)

    return render(request, "accounts/editar_perfil.html", {"form": form, "avatar_form": avatar_form})
