mi_archivo = open('prueba.txt')

print(mi_archivo.read().lower())
una_linea = mi_archivo.readline()
print(una_linea)

todas = mi_archivo.readlines()
print(todas)

mi_archivo.close()