class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('verde','Tucán')

print(mi_pajaro.especie)
print(f'Mi {mi_pajaro.especie} es de color {mi_pajaro.color}')
print(Pajaro.alas)
print(mi_pajaro.alas)

# Práctica Atributos 2
#Crea una clase llamada Cubo, y asígnale el atributo de clase:
#caras = 6
#y el atributo de instancia:
#color
#Crea una instancia cubo_rojo, de dicho color.

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')


#3
class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)