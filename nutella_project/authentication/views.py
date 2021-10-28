from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from .forms import RegisterForm
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

