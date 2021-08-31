from django.db import models

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=70)

class Products(models.Model):
	product_name = models.CharField(max_length=255)
	code = models.IntegerField()
	nutrition_grade = models.CharField(max_length=1)
	stores = models.CharField(max_length=255)
	url = models.URLField(max_length=255)
	category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

# class Substitutes(models.Model):
# 	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
# 	substitue_id = models.ForeignKey(Products, on_delete=models.CASCADE)