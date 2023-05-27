from collections import Counter

numeros = [8, 5, 3, 4, 7, 9, 0, 3, 2, 1]

frase = 'Al pan pan y al vino vino'
# cuantas veces se repite un número

print(Counter(numeros))
# Counter({3: 2, 8: 1, 5: 1, 4: 1, 7: 1, 9: 1, 0: 1, 2: 1, 1: 1})

print(Counter(frase.split()))
