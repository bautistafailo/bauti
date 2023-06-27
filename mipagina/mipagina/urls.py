"""
URL configuration for mipagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from sanLuis import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la vista de índice
    path('modalidades/', views.modalidades, name='modalidades'),
    path('busqueda_servicios/', views.busqueda_servicios, name='servicios'),
    path('buscar/', views.buscar, name="buscar"),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.crear_cliente, name='crearcliente'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




