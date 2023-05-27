palabra = 'Python'

lista = [letra for letra in palabra]
print(lista)

lista_numeros = [n for n in range(0,21)]
print(lista_numeros)

lista_pares = [n for n in range(0,41) if n%2==0]
print(lista_pares)

pies = [10,20,30,40,50]
metros = [p*3.281 for p in pies]
print(metros)
