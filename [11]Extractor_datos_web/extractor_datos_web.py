import bs4
import requests

# url sin paginación
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

for pagina in range(1, 51):

    # sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar en los libros
    for libro in libros:

        # verificar que tengan 4 o 5 estrellas
        if (len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0):

            # guardar titulos en una variable
            titulos_libros = libro.select('a')[1]['title']

            # agregar a la lista
            titulos_rating_alto.append(titulos_libros)

# mostrar los libros
for t in titulos_rating_alto:
    print(t)

