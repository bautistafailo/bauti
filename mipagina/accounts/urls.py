
from django.urls import path
from accounts import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('mostrar/', login_required(TemplateView.as_view(template_name='accounts/mostrar_account.html')), name='mostrar'),
    path('editar/', login_required(views.editar_perfil), name='editar'),
    path('about/', login_required(TemplateView.as_view(template_name='accounts/about.html')), name='about'),
    path('masinfo/', login_required(TemplateView.as_view(template_name='accounts/masinfo.html')), name='masinfo'),
]


