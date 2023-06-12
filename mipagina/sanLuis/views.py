from django.shortcuts import render
from django.http import HttpResponse
from sanLuis.models import Pago
import datetime
# Create your views here.


def busqueda_servicios(request):

    return render(request, "sanLuis/busqueda_servicios.html")

def buscar(request):

    if request.GET["nombre"]:

        #mensaje="Servicio buscado: %r" %request.GET["serv"]
        servicio=request.GET["nombre"]

        servicios = Pago.objects.filter(nombre__icontains=servicio)


        return render(request, "sanLuis/resultados_busqueda.html", {"servicios":servicios, "query":servicio})
    else:
        
        mensaje="Servicio no encontrado"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "sanLuis/gracias.html")

    return render(request, "sanLuis/contacto.html")

def index(request):
    return render(request, "sanLuis/index.html")

def modalidades(request):
    return render(request, "sanLuis/modalidades.html")



