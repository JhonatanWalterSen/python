from pathlib import Path, PureWindowsPath

#Lectura
carpeta = Path('C:/Users/Ariza/Desktop/Otro_archivo.txt')
print(carpeta.read_text())

print(carpeta.name)
#Otro_archivo.txt
print(carpeta.suffix)
#txt
print(carpeta.stem)
#Otro_archivo

#validar su existenciad de un archivo
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Si existe')

#Cambiar a ruta de windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
