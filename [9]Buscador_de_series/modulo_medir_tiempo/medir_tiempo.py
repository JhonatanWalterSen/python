import time

import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista

inicio = time.time()
print(prueba_for(15000))
final = time.time()
print(final-inicio)

inicio = time.time()
print(prueba_while(15000))
final = time.time()
print(final-inicio)


declaracion = '''
prueba_for(10)
'''
mi_setup ='''
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''

duracion=timeit.timeit(declaracion, mi_setup, number=10000)
print(duracion)

#timeit para medir precisión del codigo un tiempo mas facilde persivir