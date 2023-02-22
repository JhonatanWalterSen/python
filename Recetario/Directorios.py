import os
from pathlib import Path

ruta = os.getcwd()
# D:\python\Recetario

ruta = os.chdir('C:\\Users\\Ariza\\Desktop')
# None

ruta = os.chdir('C:\\Users\\Ariza\\Desktop')

archivo = open('Otro_archivo.txt')

#Crear carpetas distintas
nueva_carpeta = os.makedirs('C:\\Users\\Ariza\\Desktop\\Otra')

#Ruta comúesta por 2 elementos

print(archivo.read())

ruta = 'D:\python\Recetario\\prueba.txt'
elemento = os.path.dirname(ruta)
#D:\python\Recetario

#ambos elementos en una tupla
elemento = os.path.split(ruta)
#('D:\\python\\Recetario', 'prueba.txt')
print(elemento)

# Eliminar carpeta

os.rmdir('C:\\Users\\Ariza\\Desktop\\Otra')

#pathLib
carpeta = Path('C:/Users/Ariza/Desktop')
archivo = carpeta / 'Otro_archivo.txt'


mi_archivoPath = open(archivo)
print(mi_archivoPath.read())