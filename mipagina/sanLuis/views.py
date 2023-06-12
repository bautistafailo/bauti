from django.shortcuts import render
from django.http import HttpResponse
from sanLuis.models import Pago
# Create your views here.


def busqueda_servicios(request):

    return render(request, "busqueda_servicios.html")

def buscar(request):

    if request.GET["email"]:

        #mensaje="Servicio buscado: %r" %request.GET["serv"]
        servicio=request.GET["email"]

        servicios = Pago.objects.filter(nombre__icontains=servicio)


        return render(request, "resultados_busqueda.html", {"servicios":servicios, "query":servicio})
    else:
        
        mensaje="Servicio no encontrado"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")

    return render(request, "contacto.html")