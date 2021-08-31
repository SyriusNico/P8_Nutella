from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import RegisterForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		registration = RegisterForm(request.POST)
		if registration.is_valid():
			registration.save()
			messages.success(request, 'Inscription réussite')
			return redirect('myAccount')
	else:
		registration = RegisterForm()

	return render(request, 'account/register.html', {'form': registration})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            login(request, user)
            return redirect('myAccount')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'account/login.html')

def logout_view(request):
	logout(request)
	home = '/'
	return redirect(home)

def myAccount(request):
	context = {}
	return render(request, 'account/myAccount.html', context)
