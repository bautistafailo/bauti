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
from django.contrib.auth.decorators import login_required
from sanLuis.views import ModalidadList, ModalidadDetalle, ModalidadCreacion, ModalidadUpdate, ModalidadDelete
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('modalidades/', views.modalidades, name='modalidades'),
    path('busqueda_servicios/', views.busqueda_servicios, name='servicios'),
    path('buscar/', views.buscar, name="buscar"),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', login_required(views.crear_cliente), name='crearcliente'),
    path('crear_pedido/', login_required(views.crear_pedido), name='crear_pedido'),
    path('modalidad/lista/', ModalidadList.as_view(), name='modalidad_lista'),
    path('modalidad/detail/<int:pk>/', ModalidadDetalle.as_view(), name='modalidad_detail'),
    path('modalidad/crear/', ModalidadCreacion.as_view(), name='modalidad_create'),
    path('modalidad/update/<int:pk>/', ModalidadUpdate.as_view(), name='modalidad_update'),
    path('modalidad/delete/<int:pk>/', ModalidadDelete.as_view(), name='modalidad_delete'),

    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





