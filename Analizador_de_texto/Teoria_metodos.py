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
