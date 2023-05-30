import re

texto = 'si necesitas ayuda llama al 28141241421 las 24 horas al'

# palabra = 'ayuda' in texto
# print(palabra)

patron = 'nada'

busqueda = re.search(patron, texto)
# findall en caso tenga varias palabras similares

print(busqueda)


frase_numerica= ' Mi numero de telefono es 930-692-695 python'
rege = r'\d\d\d-\d\d\d-\d\d\d'
# rege = r'\d{3}-\d{3}-\d{3}'

numero_JAQ = re.search(rege, frase_numerica)
print(numero_JAQ) # <re.Match object; span=(26, 37), match='930-692-695'>
print(numero_JAQ.group()) # 930-692-695



# clave inicie

clave = input('Clave: ')
patronx = r'\D{1}\w{7}'

chequear = re.search(patronx,clave)
print(chequear)


linea = ' no se atiende los jueves en la tarde'
buscar_linea = re.search(r'lunes|martes', linea)
print(buscar_linea)

import re

import re


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")



def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")