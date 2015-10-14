from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import login, authenticate, logout

from django.core.urlresolvers import reverse, reverse_lazy

from .forms import UserLoginForm, UserCreateForm

# Create your views here.
class LogInView(FormView):

	template_name = 'users/login.html'
	form_class = UserLoginForm
	success_url = reverse_lazy('main:home')

	def form_valid(self, form):
		user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password']
			)
		if user is not None:
			if user.is_active:
				login(self.request, user)
				return super(LogInView, self).form_valid(form)


class RegisterView(CreateView):

	template_name = 'users/register.html'
	form_class = UserCreateForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		user = form.save()
		user.set_password(form.cleaned_data['password'])
		return super(RegisterView, self).form_valid(form)

def logOut(request):
	logout(request)
	return redirect(reverse('main:home'))