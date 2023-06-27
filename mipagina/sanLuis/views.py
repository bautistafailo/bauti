from django.shortcuts import render
from django.http import HttpResponse
from sanLuis.models import Pago
from django.shortcuts import render, redirect
from .models import Clientes
from .models import Pedidos




# Create your views here.


def busqueda_servicios(request):

    return render(request, "sanLuis/busqueda_servicios.html")

from django.shortcuts import render
from .models import Pago

def buscar(request):
    servicio = request.GET.get("nombre")

    if servicio:
        servicios = Pago.objects.filter(nombre__icontains=servicio)
        return render(request, "sanLuis/resultados_busqueda.html", {"servicios": servicios, "query": servicio})

    return render(request, "sanLuis/agradecimiento.html")



def contacto(request):
    if request.method=="POST":
        return render(request, "sanLuis/agradecimiento.html")

    return render(request, "sanLuis/contacto.html")

def index(request):
    return render(request, "sanLuis/index.html")

def modalidades(request):
    return render(request, "sanLuis/modalidades.html")


def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        cliente = Clientes(nombre=nombre, email=email, telefono=telefono)
        cliente.save()
        return redirect('index')
    else:
        return render(request, 'sanLuis/formulario.html')
    



def crear_pedido(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        fecha = request.POST.get('fecha')
        pagado = request.POST.get('pagado')

        pedido = Pedidos(numero=numero, fecha=fecha, pagado=pagado)
        pedido.save()

        return redirect('index')  
    else:
        return render(request, 'sanluis/pedido.html')





















