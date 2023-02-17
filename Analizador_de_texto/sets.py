#set elementos únicos, elementos inmutables
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set ={10, 20, 30}
print(type(otro_set))
print(otro_set)

#no tiene un orden interno
#Elimina los repetidos
# no acepta tipo List []
# Si adminte Tuples () por que son inmutables

print(2 in mi_set)
#union de sets
s3 = mi_set.union(otro_set)
print(s3)

#agregar un elemento al set
s3.add('hola')
print(s3)

#discard un elemento no da error si no existe
#remove quita el elemento
#clear limpiar set