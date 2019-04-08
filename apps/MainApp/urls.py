from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name="Index"),
    url(r'^Register', views.RegistrationPage, name="Register"),
    url(r'^Login', views.LoginPage, name="Login"),
    url(r'^RegistrationProcess$', views.RegistrationProcess, name="RegistrationProcess"),
    url(r'^Home$', views.Home, name="Home")
]