from django.shortcuts import render
from django.http import HttpResponseRedirect
from .offApi import OffApi
import requests


# Create your views here.
def result(request):
	api = OffApi()
	responses = requests.get(api.url, api.payload)
	offData = responses.json()

	context = {
		'product_name' : offData['product_name'],
		'code' : offData['code'],
		'nutrition_grade' : offData['nutrition_grade_fr'],
		'stores' : offData['stores'],
		'url' : offData['url']
	}
	render
	