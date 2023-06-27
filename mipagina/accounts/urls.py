
from django.urls import path
from accounts import views
from django.views.generic import TemplateView




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('editar/', views.editar_perfil, name='editar'),
    path('about/', TemplateView.as_view(template_name='accounts/about.html'), name='about'),
    path('masinfo/', TemplateView.as_view(template_name='accounts/masinfo.html'), name='masinfo'),
]


