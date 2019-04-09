from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name="Index"),
    url(r'^Register$', views.RegistrationPage, name="Register"),
    url(r'^RegistrationProcess$', views.RegistrationProcess, name="RegistrationProcess"),
    url(r'^Login$', views.LoginPage, name="Login"),
    url(r'^LoginProcess$', views.LoginProcess, name="LoginProcess"),
    url(r'^Logout$', views.Logout, name="Logout"),
    url(r'^LogoutProcess$', views.LogoutProcess, name="LogoutProcess"),
    url(r'^Home$', views.Home, name="Home")
]