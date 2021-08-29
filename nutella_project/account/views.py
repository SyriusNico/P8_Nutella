from django.shortcuts import render, redirect
from django.contrib import messages
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



def myAccount(request):
	context = {}
	return render(request, 'account/myAccount.html', context)
