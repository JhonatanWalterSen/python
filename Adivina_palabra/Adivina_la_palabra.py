from random import randint

nombre = input('¿Cual es tu nombre')
num_secreto = randint(1,101)
intentos = 0

print(f'Hola {nombre} tienes 8 intentos para adivinar un número del 1 al 100')

while intentos < 8:
    estimado = int(input('¿Cual es el número?'))
    intentos +=1

    if estimado < num_secreto:
        print("Incorrecta el número es mas alto")
    if estimado > num_secreto:
        print("Incorrecta el número es mas bajo")
    if estimado == num_secreto:
        print(f"GANASTE {nombre}! Has adivinado en {intentos} intentos ")
        break

#if estimado != num_secreto:
#    print(f'el numero secreto era {num_secreto}')