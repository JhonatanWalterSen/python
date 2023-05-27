def Sumar():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1+n2)
    print('Gracias por sumar' + n1)


try:
    Sumar()
    # código que queremos probar
except TypeError:
    print('Estas intentando concatenar tipos distintos')
    # print('Algo no salió bien EXCEPT')
    # Código a ejecutar si hay un error
except ValueError:
    print('Ese no és un número')
else:
    print('Salió bien ELSE')
    # Código a ejectuar si no hay un error
finally:
    print('Eso es Todo FINALLY')
    # Código que se va a ejecutar de todos modos
    #Se improme pase lo que pase