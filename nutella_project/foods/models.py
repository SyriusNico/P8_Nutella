from django.db import models

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name

class Products(models.Model):
	product_name = models.CharField(max_length=255)
	code = models.CharField(max_length=255)
	nutrition_grade = models.CharField(max_length=255)
	stores = models.CharField(max_length=255)
	url = models.URLField(max_length=255)
	sugar = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	salt = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	proteins = models.DecimalField(max_digits=5, decimal_places=2, default=0)
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