class Animal:
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):
    def __init__(self, edad, color,altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('PIO')
    def volar(self,metros):
        print(f'El Pajaro vuela {metros} metros')

piolin = Pajaro(2,'amarillo',40)
piolin.hablar()
piolin.volar(100)

############################ OTRO ###########################
class Madre:
    def reir(self):
        print('ja ja')
    def hablar(self):
        print('Que tal')
class Padre:
    def hablar(self):
        print('Hola')

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto=Nieto()
mi_nieto.hablar()
mi_nieto.reir()



#1
class PadreEjercicio():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class MadreEjercicio():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class HijaEjercicio(MadreEjercicio, PadreEjercicio):
    pass

#2
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave,Reptil,Pez,Mamifero):
    pass


#3
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"