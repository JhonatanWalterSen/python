#usuario ingresar un texto
# 3 letras a su elección

#1 Cuantas veces aparece la letra que eligió Recomendacion: almacenarlo en una lista pasar a minuscula
#2 Cuantas palabras hay en todo el texto
#3 primera letra del texto y la ultima
#4 mostrar como quedaria el orden de las palabras al inverso
#5 la palabra Python aparece en el texto

usuario_texto = input('Ingresa un texto').lower()
letras = []

letras.append(input('Ingresa la primera letra').lower())
letras.append(input('Ingresa la segunda letra').lower())
letras.append(input('Ingresa la tercera letra').lower())

print("\n")
print("CANTIDAD DE LETRAS REPETIDAS")
letra1 = usuario_texto.count(letras[0])
letra2 = usuario_texto.count(letras[1])
letra3 = usuario_texto.count(letras[2])

print(f"La letra '{letras[0]}' se encontró {letra1} veces")
print(f"La letra '{letras[1]}' se encontró {letra2} veces")
print(f"La letra '{letras[2]}' se encontró {letra3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
#2
palabras_texto = usuario_texto.split(' ')
print(f"hemos encontrado esta cantidad de palabras {len(palabras_texto)}")


print("\n")
print("LETRA DE INICIO Y FIN")
#3
letra_inicio = usuario_texto[0]
letra_fin = usuario_texto[-1]
print(f"Letra inicial es: '{letra_inicio}' y la letra final es: '{letra_fin}'")

print("\n")
print("TEXTO INVERSO")
#4
palabras_texto.reverse()
inverso = " ".join(palabras_texto)
print(f"inverso: '{inverso}' ")

print("\n")
print("¿APARECE Python?")
#5
buscar_python = 'python' in usuario_texto
dic = {
    True: 'si',
    False: 'no'
}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")