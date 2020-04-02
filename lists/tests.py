from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve es la función que Django usa internamente para resolver la URL
        # y encontrar cuál función de view debe mapear
        found = resolve('/')
        # Comprobamos que "/" (la raíz de la página) encuentra una función llamada home_page
        self.assertEqual(found.func, home_page)