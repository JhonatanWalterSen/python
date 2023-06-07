import pygame
import random
import math

# Inicializar PYgame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Configuraciones Titulo e Ícono
pygame.display.set_caption('Invasión Espacial (Los extraterrestres)')
icono = pygame.image.load('extraterrestre.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# puntaje
puntaje = 0

# variables del Jugador
img_jugador = pygame.image.load('pikachu.png')
posicion_x = 368
posicion_y = 520
posicion_x_cambio = 0

# variables del enemigo
img_enemigo = pygame.image.load('pokebola.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

# variables del trueno
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
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

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
                print('Flecha Izquierda <- Presionada')
            if evento.key == pygame.K_RIGHT:
                posicion_x_cambio = 0.1
                print('Flecha Derecha -> Presionada')
            if evento.key == pygame.K_SPACE:
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
    enemigo_x += enemigo_x_cambio

    # mantener dentro del borde al Enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    # movimiento trueno
    if trueno_y <= -64:
        trueno_y = 500
        bala_visible = False

    if bala_visible:
        disparar_trueno(trueno_x, trueno_y)
        trueno_y -= trueno_y_cambio

    # colision
    colision = hay_colision(enemigo_x, enemigo_y, trueno_x, trueno_y)
    if colision:
        trueno_y = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)

    jugador(posicion_x, posicion_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()