from django.test import TestCase, Client

from authentication.views import UserRegisterView

class UserRegisterViewTest(TestCase):
	def setUp(self):
		self.client = Client()

	def test_user_register_view_url(self):
		response = self.client.get('/some/url/')
		# goodResponse = self.client('/login/')
		self.assertEqual(response.status_code, 404)
		# self.assertEqual(goodResponse.status_code, 200)
