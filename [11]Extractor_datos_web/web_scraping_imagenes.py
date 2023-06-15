from random import randint

import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')

# print(imagenes)

for img in imagenes:
    random_number = randint(0, 1000)
    name = 'img_' + str(random_number) + '.jpg'
    binary_img = requests.get(img['src'])
    binary_content = binary_img.content

    img_file = open(name, 'wb')
    img_file.write(binary_content)
    img_file.close()