# 1
def devolver_distintos(a, b, c):
    suma = a+b+c
    lista=[a,b,c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(7,2,4))

#2
def letras_unicas(palabra):
    mi_set= set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas('pollito a la brasa'))

#3
def ceros_vecinos(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador]==0 and args[contador + 1] ==0:
            return True
        else:
            contador +=1

    return False

print(ceros_vecinos(6,3,5,0,4,0,5,7,3,4,0))


#4
def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    while iteracion <= numero:

        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break

        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)


print(contar_primos(50))