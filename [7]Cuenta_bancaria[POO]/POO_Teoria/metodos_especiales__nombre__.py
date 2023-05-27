mi_lista=[1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto=Objeto()
print(mi_objeto)
# <__main__.Objeto object at 0x000002C3941EC708>

class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo=titulo
        self.canciones=canciones
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return  self.canciones

    def __del__(self):
        print('Se eliminó')

mi_cd = CD('Pink','The Wall', 24)
print(len(mi_cd))
del mi_cd


#1
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

#2
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

#3
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
