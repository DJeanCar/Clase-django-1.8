from django.conf.urls import include, url
from .views import MovieDetailView


urlpatterns = [
	url(r'^peliculas/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name="movie_detail"),
]