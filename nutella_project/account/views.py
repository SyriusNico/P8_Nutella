from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
	context = {}
	return render(request, 'account/login.html', context)

def myAccount(request):
	context = {}
	return render(request, 'account/myAccount.html', context)