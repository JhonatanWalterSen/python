from random import *

aleatorio = randint(1,50)
print(aleatorio)

#floats
aleatorio = round(uniform(1,5),2)
print(aleatorio)

#floats entre 0 y 1
aleatorio = random()
print(aleatorio)

#dentro la seleccion de una lista
colores = ['verde','azul','rojo']
print(choice(colores))

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)