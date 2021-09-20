import requests
import pprint
from django.core.management.base import BaseCommand
from ...models import Categories, Products, Substitutes

class Utils():

	def lookFor(self, product):
		result = Products.objects.filter(product_name=product)
		print(result)
		return result

	def giveMeBetterThan(self, *product):
		
		betterChoice = []
		allProduct = Products.objects.all()
		isCategory = allProduct.filter(category_id=product.category_id)
		for oneProduct in isCategory:
			print(oneProduct)
		# 	if oneProduct.category_id == product.category_id:
		# 		if oneProduct.product_name == product.product_name :
		# 			pass
		# 		elif oneProduct.nutrition_grade == product.nutrition_grade:
		# 			pass
		# 		elif oneProduct.nutrition_grade == 'e':
		# 			pass 
		# 		else:
		# 			betterChoice.append(oneProduct)
		# return betterChoice


class Command(BaseCommand):

	def handle(self, *args, **options):	
		u = Utils()
		nutella = u.lookFor('nutella')
		# u.giveMeBetterThan(nutella)