from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Index, name="Index"),
    url(r'^Register$', views.RegistrationPage, name="Register"),
    url(r'^RegistrationProcess$', views.RegistrationProcess, name="RegistrationProcess"),
    url(r'^Login$', views.LoginPage, name="Login"),
    url(r'^Error$', views.ErrorPage, name="Error"),
    url(r'^LoginProcess$', views.LoginProcess, name="LoginProcess"),
    url(r'^Logout$', views.Logout, name="Logout"),
    url(r'^Home$', views.Home, name="Home"),
    url(r'^Rider/(?P<uuid>\d+)$', views.Rider, name="Rider"),
    url(r'^CreateEvent$', views.CreateEvent, name="CreateEvent"),
    url(r'^CreateEventProcess$', views.CreateEventProcess, name="CreateEventProcess"),
    url(r'^Join/(?P<id>\d+)$', views.Join, name="Join"),
    url(r'^RemoveProcess/(?P<id>\d+)$', views.RemoveUserFromEvent, name="RemoveProcess"),
    url(r'^Event/(?P<uuid>\d+)$', views.EventDetails, name="Event"),
    url(r'^Explore/$', views.Explore, name="Explore"),
    url(r'^Explore/Api$', views.ExploreApi, name="ExploreApi"),
    url(r'^DeleteEvent/(?P<id>\d+)$', views.DeleteEvent, name="DeleteEvent"),
    url(r'^ImageUpload$', views.ImageUpload, name="ImageUpload")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)