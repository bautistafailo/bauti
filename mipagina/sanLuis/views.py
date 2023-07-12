from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from .models import Pago, Clientes, Pedidos, Modalidad


# Vista basada en clase que muestra una lista de modalidades
class ModalidadList(ListView):
    model = Modalidad
    template_name = "sanLuis/modalidad_lista.html"


# Vista basada en clase que muestra los detalles de una modalidad específica
class ModalidadDetalle(DetailView):
    model = Modalidad
    template_name = "sanLuis/detail.html"


# Vista basada en clase para crear una nueva modalidad
class ModalidadCreacion(CreateView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha', 'imagen']
    template_name = "sanLuis/modalidad_form.html"


# Vista basada en clase para actualizar una modalidad existente
class ModalidadUpdate(UpdateView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha', 'imagen']
    template_name = "sanLuis/modalidad_form.html"


# Vista basada en clase para eliminar una modalidad existente
class ModalidadDelete(DeleteView):
    model = Modalidad
    success_url = reverse_lazy('modalidad_lista')
    template_name = "sanLuis/delete.html"


# Vista que muestra la página de búsqueda de servicios (requiere inicio de sesión)
@login_required
def busqueda_servicios(request):
    return render(request, "sanLuis/busqueda_servicios.html")


# Vista que realiza la búsqueda de servicios y muestra los resultados (requiere inicio de sesión)
@login_required
def buscar(request):
    servicio = request.GET.get("nombre")

    if servicio:
        servicios = Pago.objects.filter(nombre__icontains=servicio)
        return render(request, "sanLuis/resultados_busqueda.html", {"servicios": servicios, "query": servicio})

    return render(request, "sanLuis/agradecimiento.html")


# Vista de contacto que muestra el formulario de contacto y procesa el envío (requiere inicio de sesión)
@login_required
def contacto(request):
    if request.method == "POST":
        return render(request, "sanLuis/agradecimiento.html")

    return render(request, "sanLuis/contacto.html")


# Vista de inicio que muestra la página de inicio (requiere inicio de sesión)
@login_required
def index(request):
    return render(request, "sanLuis/index.html")


# Vista de modalidades que muestra la página de modalidades (requiere inicio de sesión)
@login_required
def modalidades(request):
    return render(request, "sanLuis/modalidades.html")


# Vista para crear un nuevo cliente (requiere inicio de sesión)
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


# Vista para crear un nuevo pedido (requiere inicio de sesión)
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






















