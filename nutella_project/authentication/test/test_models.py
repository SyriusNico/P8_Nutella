from django.test import TestCase
from authentication.forms import RegisterForm, LoginForm

"""
EXAMPLE
"""
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(True)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


class RegisterFormTest(TestCase):

	def test_register_form_field(self):
		name = 123
		email = 123
		form = RegisterForm(data={'username': name,
								  'email' : email})
		self.assertFalse(form.is_valid())

	def test_register_form_field_empty(self):
		form = RegisterForm(data={'username': None,
								  'email': None,})
		self.assertIsNotNone(form.fields['username'])
		self.assertIsNotNone(form.fields['email'])



class LoginFormTest(TestCase):

	def test_register_form_field_label(self):
		form = RegisterForm()
		self.assertTrue(
			form.fields['username'].label == None or \
			form.fields['username'].label == "Nom d'utilisateur"
			)