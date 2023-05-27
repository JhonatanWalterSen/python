def pedir_numero():

    while True:
        try:
            numero = int(input('Ingresa un número: '))
        except:
            print(' Ese no es un Número')
        else:
            print(f'Ingresaste el número {numero}')
            break
    print('Gracias')

pedir_numero()

#145
def suma(num1,num2):
    try:
        num1+num2
    except:
        print('Error inesperado')
    else:
        print(num1+num2)

#146
def cociente(num1,num2):

    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

#147
def abrir_archivo(nombre_archivo):

    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")


#MENSAJES EN PANTALLA:
"El archivo no fue encontrado"
"Error desconocido"
"Abriendo exitosamente"
"Finalizando ejecución"