from django.db import models

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=70)

	def __str__(self):
		return self.name

class Products(models.Model):
	product_name = models.CharField(max_length=255)
	code = models.IntegerField()
	nutrition_grade = models.CharField(max_length=1)
	stores = models.CharField(max_length=255)
	url = models.URLField(max_length=255)
	category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

	def __str__(self):
		return self.product_name

class Substitutes(models.Model):
	choosen_product = models.ForeignKey(Products, on_delete=models.CASCADE,
											related_name='choosen_product')
	substitue = models.ForeignKey(Products, on_delete=models.CASCADE,
											 related_name='substitute')
	def __str__(self):
		return self.substitue