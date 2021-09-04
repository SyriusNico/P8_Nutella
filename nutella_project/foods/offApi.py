# coding: utf-8
from foods.models import Categories, Products

class OffApi():

	def __init__(self):

		self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'
		self.category = [
			'Produit à tartiner',
			'Petit-déjeuners',
			'sauces',
			'fromages',
			'legumineuses'
			]
		self.page_size = 50

	def payload(self, category):
		payload = {
			'action': 'process',
			'tagtype_0': 'categories',
			'tag_contains_0': 'contains',
			'tag_0': category,
			'tagtype_1': 'nutrition_grade_fr',
			'tag_contains_1': 'contains',
			'page_size': self.page_size,
			'json': 'true',
		}
		return payload


	def getProductsFromOff(self, category):


		payload = self.payload(category)
		req = requests.get(self.url, payload)
		products = req.json().get('products')

		return products

	def getProductsByCategory(self):

		for category in self.category:
			productsByCategory = self.getProductsFromOff(category)

		return productsByCategory


	def storeDatas(self):

		for category in self.category:
			products = self.getProductsFromOff(category)
			categoryData = Categories(name=category)
			categoryData.save()
			for product in products:
				productData = Products(
					product_name=product.get('product_name'),
					code=product.get('code'),
					nutrition_grade=product.get('nutrition_grade_fr'),
					stores=product.get('stores'),
					url=product.get('url')
				)

