# FOR
nombres = ['Juan','Ana','Carlos','Belén','Fran']
print('####### 1 #######')
for nombre in nombres:
    numero_nombre = nombres.index(nombre) +1
    print(f'Hola {nombre}: indice {numero_nombre}')


print('####### 2 #######')
lista = ['pablo','james','joel']
for nombress in lista:
    if nombress.startswith('j'):
        print(nombress)
    else:
        print(f'{nombress} no inicia con J')

print('####### 3 #######')
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

print('####### 4 #######')

palabras = 'python'
for letr in palabras:
    print(letr)

print('####### 5 #######')

dic = {
    'clave':'a',
    "clave2":'b',
    "clave3":'c'
}

for item in dic:
    print(item)

#completos
for item in dic.items():
    print(item)

#valores
for item in dic.values():
    print(item)