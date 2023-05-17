class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    def pintar_negro(self):
        self.color='negro'
        print(f'Ahora el pajaro es de color {self.color}')

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        #no se relaciona con las instancias
        print('El Pajaro Mira')
#piolin = Pajaro('amarillo','canario')
#piolin.volar(50)
#piolin.alas = False
#print(piolin.alas)
#Pajaro.poner_huevos(3)
Pajaro.mirar()


#1
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#2
class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

#3
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1

