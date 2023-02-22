import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),'Recetas')

#Cuantas recetas hay
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador

def inicio():
    system('cls')
    print('*'*50)
    print(f'***** Bienvenido al Administrador de recetas *****')
    print('*'*50)
    print('\n')
    print(f'Las recetas se encuentras ubicadas en {mi_ruta}')
    print(f' Total recetas: {contar_recetas(mi_ruta)}')
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opción:')
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar Categoría
        [6] - Salir del programa
        ''')
        eleccion_menu = input()
    return  eleccion_menu

#inicio()

def mostrar_categorias(ruta):
    print('Categorias:')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador +=1
    return lista_categorias



def elegir_categoria(lista):
    eleccion_correcto = 'x'
    while not eleccion_correcto.isnumeric() or int(eleccion_correcto) not in range(1,len(lista)):
        eleccion_correcto = input('\n Elige una categoria:')

    return lista[int(eleccion_correcto)-1]

# mostrar menu de inicio
menu = 0

if menu ==1:
    mis_categorias=mostrar_categorias(mi_ruta)
    mi_categoria=elegir_categoria(mis_categorias)
    # mostrar recetas
    # elegir recetas
    # leer recetas
    # volver al inicio
    pass
elif menu == 2:
    mis_categorias=mostrar_categorias(mi_ruta)
    mi_categoria=elegir_categoria(mis_categorias)
    # crear receta nueva
    # volver al inicio
    pass
elif menu == 3:
    #crear categoria
    #volver al inicio
    pass
elif menu ==4:
    mis_categorias=mostrar_categorias(mi_ruta)
    mi_categoria=elegir_categoria(mis_categorias)
    # mostrar recetas
    # elegir recetas
    # Eliminar recetas
    # volver al inicio
    pass
elif menu == 5:
    mis_categorias=mostrar_categorias(mi_ruta)
    mi_categoria=elegir_categoria(mis_categorias)
    # eliminar cat
    # volver inicio
    pass
elif menu ==6:
    # finalizar programa
    pass