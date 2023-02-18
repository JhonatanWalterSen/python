lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice+=1

#Manera Correcta
for ind,it in enumerate(lista):
    print(ind,it)

#transformar  a tuplas
mis_tuplas=list(enumerate(lista))
print(mis_tuplas)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)