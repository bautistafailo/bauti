from django.http import HttpResponse 
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from accounts.models import Accounts

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido=apellido
        

def saludo(request): #primera vista
    p1=Persona("Fernanda", "Passini",)

    #director="Fernanda"

    #apellido="Passini"
    
    vicesescuela=["Amalia Herrera", "Paula Isnaldi"]

    horit=datetime.datetime.now()

    return render(request, "miplantilla.html", ({"directora": p1.nombre,"apellidos": p1.apellido, "hora": horit, "vices": vicesescuela}) )

def nosotros(request):
    fecha_ahora = datetime.datetime.now()
    return render(request, "nosotros.html", {"horit": fecha_ahora})

def modalidades(request):
    fecha_ahora = datetime.datetime.now()
    return render(request, "modalidades.html", {"horit": fecha_ahora})

def despedida(request):


    return HttpResponse("Chau perros")


def lahora(request):
    fecha_ahora = datetime.datetime.now()
    documento = """
    <html>
    <body>
    <h1>
    Horario actual: %s
    </h1>
    </body>
    </html>""" % fecha_ahora

    return HttpResponse(documento)



def calculaedad(request, agno):
    edadactual = 18
    periodo = agno - 2023
    edadfutura = edadactual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años." % (agno, edadfutura)
    

    return HttpResponse(documento)


def inicio(request):
    try:
        url = Accounts.objects.filter(id=request.user.id)[0]
    except IndexError: 
        url = None   
    return render(request, "sanLuis/index.html", {"url": url})


