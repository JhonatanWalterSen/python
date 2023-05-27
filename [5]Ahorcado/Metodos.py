def saludar_persona(x):
    print('hola' +x)

saludar_persona('Walter')

#return
def multiplicar(n1,n2):
    total = n1*n2
    return total

resultado = multiplicar(10,20)
print(resultado)


#Funciones dinámicas
def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)

def chequear(lista):
    listas=[]
    for n in lista:
        if n in range(100,1000):
            listas.append(n)
        else:
            pass
    return listas

resul = chequear([312,351,566])
print(resul)

#Ejemplo de funciones
precios_cafe=[('capucchino',1.5),('expreso',5.2),('moca',1.9)]

for elemento in precios_cafe:
    print(elemento)

def cafe_caro(lista_precios):
    precio_mayor=0
    cafe_caro=''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro=cafe
        else:
            pass

    return (cafe_caro,precio_mayor)

print(cafe_caro(precios_cafe))

