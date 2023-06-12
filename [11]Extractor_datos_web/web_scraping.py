import bs4
import requests


resultado = requests.get('https://escueladirecta-blog.blogspot.com')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title')[0].getText())

parrafo_destacado = sopa.select('h3')[1].getText()
print(parrafo_destacado)