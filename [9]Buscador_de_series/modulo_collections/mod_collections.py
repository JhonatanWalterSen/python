from collections import Counter, defaultdict, namedtuple

numeros = [8, 5, 3, 4, 7, 9, 0, 3, 2, 1]

frase = 'Al pan pan y al vino vino'
# cuantas veces se repite un número

print(Counter(numeros))
# Counter({3: 2, 8: 1, 5: 1, 4: 1, 7: 1, 9: 1, 0: 1, 2: 1, 1: 1})

print(Counter(frase.split()))

mi_dic = defaultdict(lambda: 'Nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

mi_tupla = (500, 18, 55)
print(mi_tupla[1])


Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)