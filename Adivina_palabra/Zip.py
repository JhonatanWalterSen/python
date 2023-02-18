nombres = ['ana','hugo','val']
edades = [23,65,32]
ciudades = ['lima','madrid','mexico']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y es de {ciudad}')

#for pais, capital in zip(paises, capitales):
#    print(f"La capital de {pais} es {capital}")