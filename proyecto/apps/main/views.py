from django.shortcuts import render
from django.views.generic import TemplateView
from apps.movies.models import Movie

# Create your views here.
# def home(request):
# 	return render(request, 'main/home.html')

class Home(TemplateView):

	template_name = 'main/home.html'

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['movies'] = Movie.objects.all()
		return context