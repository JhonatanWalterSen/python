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