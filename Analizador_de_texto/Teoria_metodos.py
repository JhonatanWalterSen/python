# Index() busca el indice de un caracter
mi_texto = "Esto es una prueba"
resultado = mi_texto[0]
print(resultado)
#E

resultado_metodo = mi_texto.index("n")
print(resultado_metodo)
#9

res = mi_texto.index("a")
print(res)
#10

res2 = mi_texto.index("a",11)
print(res2)
#17

#index (¿Que buscar?, de donde inicia, hasta donde acaba)
#rindex() busca de derecha a izquierda

## Extraer SubString
texto= "ABCDEFGHI"
fragmento = texto[2:5]
#Etraer del indice 2 al 5
print(fragmento)

text = "Este es el texto de Jhonatan"
resul = text

print(resul)

#transformar a mayusculas
print(resul.upper())

#Separar en elementos en una lista
print(resul.split(" "))


#join()

a= "Aprender"
b= "Python"
c= "es"
d= "genial"
e= " ".join([a,b,c,d])
print(e)

#find() buscar un determinado caracter da resultado la posicion o -1

conFind = e.find('x')
print(conFind)


#replace
replaceResult = e.replace("Python", "C#")
print(replaceResult)


frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
print(frase.replace("mala","buena").replace("difícil", "fácil"))

nombre = "carina"
print(nombre*5)

#Salto de linea en los Strings
poema="""Mil pequeños  
    peces
    blancos"""
print(poema)

print("peces" in poema)

print("peces" not in poema)
print(len(poema))


#Listas
lista = ['a','b','c']
lenLista = len(lista)
print(lenLista)



#Diccionarios

diccionario = {
    'c1': 'valor1',
    'c2': 'valor1'
}
resulta=diccionario['c1']

print(diccionario)
print(resulta)


cliente ={
    'nombre':'juan',
    'apellido':'Fuentes',
    'peso': 24,
    'talla': 1.76
}

consulta = cliente['apellido']
print(consulta)

#Tuplas ocupan menos espacio que las listas
tuple = (1,2,(10,20),4)
print(type(tuple))

print(tuple[0])
print(tuple[-2]) # derecha a izquierda
#son inmutables
cambio_tuple = list(tuple)
print(type(cambio_tuple))


t= (1,2,3,1)

#Cuantas veces aparece el 1
print(len(t.count(1)))

print(t.index(1))

x,y,z= t
print(x,y,z)