from selenium import webdriver
# Webdriver para abrir una ventana de Firefox
browser = webdriver.Firefox()
# Usando el webdriver para abrir una página web del PC local
browser.get('http://localhost:8000')
# Comprobando que la página tiene "Django" en su título
assert 'Django' in browser.title