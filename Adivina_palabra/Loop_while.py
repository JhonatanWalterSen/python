monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas = monedas - 1


respuesta = "s"

while respuesta == "s":
    respuesta = input('quieres seguir? (s/n)')
else:
    print('Gracias')