from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name="Index"),
    url(r'^Register$', views.RegistrationPage, name="Register"),
    url(r'^RegistrationProcess$', views.RegistrationProcess, name="RegistrationProcess"),
    url(r'^Login$', views.LoginPage, name="Login"),
    url(r'^LoginProcess$', views.LoginProcess, name="LoginProcess"),
    url(r'^Logout$', views.Logout, name="Logout"),
    url(r'^Home$', views.Home, name="Home"),
    url(r'^Rider/(?P<id>\w+)$', views.UserProfile, name="Rider"),
    url(r'^CreateEvent$', views.CreateEvent, name="CreateEvent"),
    url(r'^CreateEventProcess$', views.CreateEventProcess, name="CreateEventProcess"),
    url(r'^Join/(?P<id>\d+)$', views.Join, name="Join"),
    url(r'^RemoveProcess/(?P<id>\d+)$', views.RemoveUserFromEvent, name="RemoveProcess"),
    url(r'^Event/(?P<id>\d+)$', views.EventDetails, name="Event"),
    url(r'^Explore/$', views.Explore, name="Explore"),
    url(r'^Explore/Api$', views.ExploreApi, name="Explore/Api")

]