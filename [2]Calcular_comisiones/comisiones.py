# Nombre y ventas

nombre = input('¿Cual es tu Nombre?')
ventas = input('¿Cuanto vendiste este mes?')
comision = round(float(ventas) * 0.13,2) + float(ventas)
print(f'Hola {nombre} tus ventas fueron de un total de {ventas} obteniendo un total de {comision} con tus comisiones')