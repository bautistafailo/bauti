from django.shortcuts import render
from accounts.models import Accounts
from sanLuis.models import Modalidad

def inicio(request):
    try:
        url = Accounts.objects.filter(id=request.user.id)[0]
        modalidad = Modalidad.objects.first()  # Obtener el primer objeto Modalidad
    except IndexError:
        url = None
        modalidad = None
    print(url)  # Imprimir el valor de 'url' en la consola
    return render(request, "sanLuis/index.html", {"url": url, "modalidad": modalidad})

