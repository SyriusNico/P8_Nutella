from django.core.management.base import BaseCommand
from ...models import Categories, Products, Substitutes

def clearDatas():

	Categories.objects.all().delete()
	Products.objects.all().delete()

class Command(BaseCommand):

	def handle(self, *args, **options):

		clearDatas()
		print("Les données ont été supprimé")