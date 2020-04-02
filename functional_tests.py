from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # Webdriver para abrir una ventana de Firefox
        # Usando el webdriver para abrir una página web del PC local
    def tearDown(self):
        # Este método cerrará la ventana de Firefox aunque haya un error durante el test
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ha oído hablar sobre una nueva aplicación online de "cosas por hacer". Ella
        # entra a ver su página principal
        self.browser.get('http://localhost:8000')
        # Comprobando que la página tiene "Django" en su título
        # Ella comprueba que el título y la cabecera de la página mencionan listas de "cosas por hacer"
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # Ella es invitada a introducir a "to-do" item directamente

        # Ella escribe "Comprar plumas de pavo real" en un recuadro.

        # Cuando ella presiona Enter, la página se actualiza, y ahora la página lista
        # "1: Comprar plumas de pavo real" como un item en una lista "to-do"

        # Todavía hay un recuadro invitándola a añadir otro item. Ella
        # introduce "Usar plumas de pavo real para volar"

        # La página se actualiza de nuevo, y ahora muestra ambos items en su lista

        # Edith se pregunta si la página recordará su lista. Entonces ve que la página ha 
        # generado una URL única para ella -- hay algún texto que explica esto

        # Ella visita esa URL - su lista "to-do" sigue ahí

        # Satisfecha, se va a dormir
if __name__ == "__main__":
    # Encontrará clases de tests y métodos y los iniciará
    unittest.main(warnings = 'ignore')

