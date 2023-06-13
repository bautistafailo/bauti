from django.shortcuts import render
from django.http import HttpResponse
from sanLuis.models import Pago




# Create your views here.


def busqueda_servicios(request):

    return render(request, "sanLuis/busqueda_servicios.html")

def buscar(request):
    servicio = request.GET.get("nombre")

    if servicio:
        servicios = Pago.objects.filter(nombre__icontains=servicio)
        return render(request, "sanLuis/resultados_busqueda.html", {"servicios": servicios, "query": servicio})

    mensaje = "Gracias por ayudarnos a mejorar!"
    return HttpResponse(mensaje)

    

def contacto(request):
    if request.method=="POST":
        return render(request, "sanLuis/gracias.html")

    return render(request, "sanLuis/contacto.html")

def index(request):
    return render(request, "sanLuis/index.html")

def modalidades(request):
    return render(request, "sanLuis/modalidades.html")

from django.shortcuts import render, redirect
from .models import Clientes
from django import forms


from django.shortcuts import render, redirect
from .models import Clientes


def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        cliente = Clientes(nombre=nombre, email=email, telefono=telefono)
        cliente.save()
        return redirect('inicio')
    else:
        return render(request, 'sanLuis/formulario.html')


















