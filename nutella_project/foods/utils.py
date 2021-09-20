from django.db.models import Q
from .models import Categories, Products, Substitutes


class Utils():

	def lookFor(self, product):
		result = Products.objects.filter(product_name=product)
		return result.category_id

	def giveMeBetterThan(self, product):

		if product in Products.objects.all():		
			try:
				prod = Products.objects.filter(category_id=product.category_id)
				if product.nutrition_grade == 'e' or product.nutrition_grade == 'd':
					sub = prod.filter(
					Q(nutrition_grade='a') | Q(nutrition_grade='b') | Q(nutrition_grade='c'))
					return sub
				if product.nutrition_grade == 'c':
					sub = prod.filter(
					Q(nutrition_grade='a') | Q(nutrition_grade='b'))
					return sub
				if product.nutrition_grade == 'b':
					sub = prod.filter(nutrition_grade='a')
					return sub

			except Products.MultipleObjectsReturned:
				pass
		else:
			return "Le produit n'est pas dans la base de données."
