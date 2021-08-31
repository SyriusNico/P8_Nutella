from django.shortcuts import render

# Create your views here.
def result(request):
	context = {}
	return render(request, 'foods/result.html', context)