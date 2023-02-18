if 5 == 2:
    print('es correcto')
else:
    print('No es correcto')

mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

#Anidando condiciones
edad = 16
cali = 9
if edad < 18:
    print('Eres menor de edad')
    if cali >= 7:
        print('Aprobado')
    else:
        print('No Aprobado')
else:
    print("Eres adulto")