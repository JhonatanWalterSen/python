def mi_dunction():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista


def mi_generador():
    for x in range(1,5):
        yield x*10

print(mi_dunction())
print(mi_generador())


g = mi_generador()

print(next(g))
print(next(g))





def mi_gen():
    x = 1
    yield x

    x += 1
    yield  x

    x += 1
    yield  x

ge = mi_gen()
print(next(ge))
print(next(ge))
print(next(ge))




#148
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()


def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1


generador2 = multiplos_siete()



def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()