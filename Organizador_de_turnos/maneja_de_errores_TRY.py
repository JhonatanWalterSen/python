def Sumar():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1+n2)
    print('Gracias por sumar')


try:
    Sumar()
    # código que queremos probar
except:
    print('Algo no salió bien EXCEPT')
    # Código a ejecutar si hay un error
else:
    print('Salió bien ELSE')
    # Código a ejectuar si no hay un error
finally:
    print('Eso es Todo FINALLY')
    # C´´odigo que se va a ejecutar de todos modos