import pygame
import random
import math
from pygame import mixer

# Inicializar PYgame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Configuraciones Titulo e Ícono
pygame.display.set_caption('Invasión Espacial (Los extraterrestres)')
icono = pygame.image.load('extraterrestre.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# Agregar musica
mixer.music.load('pokemon-intro.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("Juego Terminado", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

# función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# variables del Jugador
img_jugador = pygame.image.load('pikachu.png')
posicion_x = 368
posicion_y = 520
posicion_x_cambio = 0

# variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigo = 8

for e in range(cantidad_enemigo):
    img_enemigo.append(pygame.image.load('pokebola.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# variables del trueno
truenos = []
img_trueno = pygame.image.load('destello.png')
trueno_x = 0
trueno_y = 520
trueno_x_cambio = 0
trueno_y_cambio = 1
bala_visible = False

# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# función disparar Trueno
def disparar_trueno(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_trueno, (x + 16, y + 10))
# Funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# Loop del juego
acaba = True
while acaba:
    # Fondo de imagen
    pantalla.blit(fondo, (0, 0))

    # iterar eventos

    for evento in pygame.event.get():

        # cerrar programa
        if evento.type == pygame.QUIT:
            acaba = False

        # presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicion_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                posicion_x_cambio = 0.1
            if evento.key == pygame.K_SPACE:
                sonido_trueno = mixer.Sound('disparo.mp3')
                sonido_trueno.play()
                nuevo_trueno = {
                    "x": posicion_x,
                    "y": posicion_y,
                    "velocidad": -1
                }
                truenos.append(nuevo_trueno)
                if not bala_visible:
                    trueno_x = posicion_x
                    disparar_trueno(trueno_x, trueno_y)

        # soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                posicion_x_cambio = 0

    # modificar ubicación del jugador
    posicion_x += posicion_x_cambio

    # mantener dentro del borde al jugador
    if posicion_x <= 0:
        posicion_x = 0
    elif posicion_x >= 736:
        posicion_x = 736

    # modificar ubicación del Enemigo
    for e in range(cantidad_enemigo):

        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigo):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener dentro del borde al Enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        for trueno in truenos:

            colision = hay_colision(enemigo_x[e], enemigo_y[e], trueno['x'], trueno['y'])
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                trueno_y = 500
                bala_visible = False
                puntaje += 1

                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento trueno
    for trueno in truenos:
        trueno['y'] += trueno['velocidad']
        pantalla.blit(img_trueno, (trueno['x'] + 16, trueno['y'] + 10))
        if trueno['y'] < 0:
            truenos.remove(trueno)

        #if trueno_y <= -64:
            #trueno_y = 500
            #bala_visible = False

    if bala_visible:
        disparar_trueno(trueno_x, trueno_y)
        trueno_y -= trueno_y_cambio



    jugador(posicion_x, posicion_y)
    mostrar_puntaje(texto_x,texto_y)

    # Actualizar
    pygame.display.update()