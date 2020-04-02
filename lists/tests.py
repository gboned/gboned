from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve es la función que Django usa internamente para resolver la URL
        # y encontrar cuál función de view debe mapear
        found = resolve('/')
        # Comprobamos que "/" (la raíz de la página) encuentra una función llamada home_page
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Creamos objeto HttpRequest, que es lo que Django ve cuando el navegador de un
        # usuario pide una página
        request = HttpRequest()
        # Lo pasamos a nuestra vista home_page, que devuelve una respuesta
        response = home_page(request)
        # Extraemos el .content de la respuesta, con decode lo convertimos a HTML
        html = response.content.decode('utf8')
        # El fichero HTML debe empezar con <html>
        self.assertTrue(html.startswith('<html>'))
        # Debe contener el título de la página
        self.assertIn('<title>To-Do lists</title>', html)
        # Y debe terminar con </html>
        self.assertTrue(html.endswith('</html>'))