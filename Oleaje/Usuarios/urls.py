from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

from .views import home

urlpatterns = [
    url(r'signup$', views.SignUp.as_view(), name='signup'),
    url(r'home$', home, name="Usuarios_home"),
    url(r'login$',
    LoginView.as_view(template_name = "Usuarios/login_form.html"),
    name = "Usuarios_login"),
    url(r'logout$', LogoutView.as_view(), name = "Usuarios_logout")
]
