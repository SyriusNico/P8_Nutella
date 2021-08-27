from django.shortcuts import render

def home(request):
	context = {}
	return render(render, 'pages/home.html', context)
