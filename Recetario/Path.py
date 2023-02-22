from pathlib import Path

#construir una ruta
base = Path.home()
guia = Path(base,"Europa","España", Path('barcelona','Sagrada_familia.txt'))
guia2 = guia.with_name("La_pedrera.txt")
print(guia)
#C:\Users\Ariza\Europa\España\barcelona\Sagrada_familia.txt
print(guia2)
#C:\Users\Ariza\Europa\España\barcelona\La_pedrera.txt
print(guia.parent)
#Trae el antecesor de una guia
# C:\Users\Ariza\Europa\España\barcelona

guiaPrueba = Path('Europa','España','Barcelona','Sagrada_familia.txt')
en_europa=guiaPrueba.relative_to('Europa')
en_espania=guiaPrueba.relative_to('Europa','España')
print(en_europa)
print(en_espania)


