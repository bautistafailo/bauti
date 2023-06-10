from django.http import HttpResponse 
import datetime

def saludo(request): #primera vista

    documento= """˂html˃
    ˂body˃
    ˂h1˃
    Hola Perro!
    ˂h1˃
    ˂body˃
    ˂html˃"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Chau perros")

def lahora(request):
    
    fecha_ahora=datetime.datetime.now()
    documento= """˂html˃
    ˂body˃
    ˂h1˃
    Horario actual! %s
    ˂h1˃
    ˂body˃
    ˂html˃""" % fecha_ahora

    return HttpResponse(documento)

def calculaedad(request, agno):

    edadactual=18
    periodo= agno - 2019
    edadfutura= edadactual+periodo
    documento="en el año %s tendras %s años" %(agno, edadfutura)

    return HttpResponse(documento)
