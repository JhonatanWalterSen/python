archivo = open('prueba-for.txt', 'a')

archivo.write('''Hola
mundo
estoy}
 allá''')

#Lineas de Strings
archivo.writelines(['Hola','mundo','aqui'])

nombres = ['pepe','Lucho','Efe']
for n in nombres:
    archivo.writelines(n+'\n')

archivo.write('Sencillo')

archivo.close()