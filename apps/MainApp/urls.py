from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register', views.RegistrationPage, name="register"),
    url(r'login', views.LoginPage, name="login")
]