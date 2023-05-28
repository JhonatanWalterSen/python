import os
import shutil
# dirección actual
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba xd')
archivo.close()

# ver los que hay
print(os.listdir())

# mover a otra ruta
shutil.move('curso.txt', 'la ruta')

# eliminar con os
# unlink eliminar un archivo en una ruta
# os.unlink()

# eliminar una carpeta vacia en una ruta
# os.rmdir()

# eliminar  la carpeta con ttodo lo que tenga adentro
# shutil.rmtree()

ruta = 'D:\\python\\Organizador_de_turnos\\unittest'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpeta son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arc in archivo:
        print(f'\t{arc}')
    print('\n')
