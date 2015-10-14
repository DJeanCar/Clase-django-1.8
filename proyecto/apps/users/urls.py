from django.conf.urls import url
from .views import LogInView, RegisterView
from . import views

urlpatterns = [
	url(r'^ingresar/$', LogInView.as_view(), name='login'),
	url(r'^registrar/$', RegisterView.as_view(), name='register'),
	url(r'^salir/$', views.logOut, name='logout'),
]
