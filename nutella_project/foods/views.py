from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Categories, Products, Substitutes
from .utils import Utils
import requests


# Create your views here.
def result(request):
	utils = Utils()
	try:
		if request.method == 'POST':
			searched = request.POST.get('searched', False)
			product = Products.objects.filter(product_name__icontains=searched).first()
			substitutes_list = utils.giveMeBetterThan(product)
			if substitutes_list == None:
				substitutes = searched
				return render(request, 'foods/result.html',
				{
					'product' : product,
					'searched' : searched
				}
				)
			else:
				substitutes = substitutes_list[:6]
				return render(request, 'foods/result.html',
				{
					'product' : product,
					'substitutes' : substitutes,
					'searched' : searched
				}
				)
		else:
			return render(request, 'foods/pageNotFound.html')
	except AttributeError:
		pass


def detail(request, product_id):
	product = Products.objects.filter(id=product_id)
	return render(request, 'foods/detail.html', {'product':product})