from django.shortcuts import render
from django.http import HttpResponse
from sanLuis.models import Pago
from django.shortcuts import render, redirect
from .models import Clientes
from .models import Pedidos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from .models import Modalidad
from django.contrib.auth.decorators import login_required



class ModalidadList(ListView):
    model = Modalidad
    template_name = "sanLuis/modalidad_lista.html"


class ModalidadDetalle(DetailView):
    model = Modalidad
    template_name = "sanLuis/detail.html"


class ModalidadCreacion(CreateView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha', 'imagen']
    template_name = "sanLuis/modalidad_form.html"



class ModalidadUpdate(UpdateView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha', 'imagen']
    template_name = "sanLuis/modalidad_form.html"




class ModalidadDelete(DeleteView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    template_name = "sanLuis/delete.html"




@login_required
def busqueda_servicios(request):

    return render(request, "sanLuis/busqueda_servicios.html")

from django.shortcuts import render
from .models import Pago

@login_required
def buscar(request):
    servicio = request.GET.get("nombre")

    if servicio:
        servicios = Pago.objects.filter(nombre__icontains=servicio)
        return render(request, "sanLuis/resultados_busqueda.html", {"servicios": servicios, "query": servicio})

    return render(request, "sanLuis/agradecimiento.html")


@login_required
def contacto(request):
    if request.method=="POST":
        return render(request, "sanLuis/agradecimiento.html")

    return render(request, "sanLuis/contacto.html")

def index(request):
    return render(request, "sanLuis/index.html")

@login_required
def modalidades(request):
    return render(request, "sanLuis/modalidades.html")

@login_required
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
    


@login_required
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





















