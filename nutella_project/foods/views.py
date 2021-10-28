from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.conf import settings
from authentication.models import User
from .forms import SearchForm
from .models import Categorie, Product, Favorite
from .utils import Utils




class ProductDetailView(DetailView):

	context_object_name = 'product'
	queryset = Product.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)
	# TODO : Add link to the product

class ResultView(ListView):
	template_name = 'foods/result.html'
	model = Product
	utils = Utils()


	def get_queryset(self):
		query = self.request.GET.get('searched')
		if query:
			print(User.username)
			object_list = self.model.objects.filter(product_name__icontains=query)
		else:
			object_list = self.model.objects.none()
		return object_list[:1]

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context

		context = super().get_context_data(**kwargs)
		query = self.request.GET.get('searched')
		subs_list = self.utils.giveMeBetterThan(query)
		try:
			context['favorites_list'] = subs_list[:6]
		except TypeError:
			context['favorites_list'] = subs_list
		return context 

	# requires user to be logged in (done)
	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		else:
			productToAdd = self.request.POST.get('save', False)
			first_pick = self.model.objects.filter(
				product_name__icontains=self.request.GET.get('searched')
				).first()
			sub = self.model.objects.get(product_name=productToAdd)
			favorite = Favorite.objects.create(
				customer=User.objects.get(id=request.user.id),
				favorite=sub)
			return render(request, 'foods/success.html', {'favorite':favorite})


# def favorites(request):
# 	if request.method == 'POST':
# 		productToSave = request.POST.get('save', False)
# 		subs = Product.objects.filter(product_name=productToSave)
# 		# copy past example not the definitive variable
# 		# new_product = subs.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
# 		return render(request, 'foods/favorites.html', { 'subs' : subs})


class ProfilePageView(TemplateView):
	template_name = 'foods/profile.html'

class FavoritesPageView(LoginRequiredMixin, ListView): 
	template_name = 'foods/favorites.html'
	context_object_name = 'favorites_list'

	def get_queryset(self):
		return Favorite.objects.filter(customer=self.request.user)	


