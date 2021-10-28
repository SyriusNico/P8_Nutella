from django.test import RequestFactory, TestCase
from .views import ResultView


class ResultViewTest(TestCase):
    def test_favorites_list_set_in_context(self):
        request = RequestFactory().get('foods/result')
        view = ResultView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('favorites_list', context)