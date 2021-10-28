from django.shortcuts import render
from django.views.generic.base import TemplateView

# def index(request):
# 	return render(request, 'pages/index.html')

class IndexView(TemplateView):
	template_name = 'pages/index.html'