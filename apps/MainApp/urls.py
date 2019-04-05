from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^Register', views.RegistrationPage, name="register"),
    url(r'^Login', views.LoginPage, name="login"),
    url(r'^RegistrationProcess$', views.RegistrationProcess, name="RegistrationProcess"),
    url(r'^Home$', views.Home, name="home")
]