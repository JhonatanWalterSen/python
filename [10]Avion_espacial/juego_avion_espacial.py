import pygame
# Inicializar PYgame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Configuraciones Titulo e Ícono
pygame.display.set_caption('Invasión Espacial (Los extraterrestres)')
icono = pygame.image.load('extraterrestre.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load('pikachu.png')
posicion_x = 368
posicion_y = 536
posicion_x_cambio = 0

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del juego
acaba = True
while acaba:
    pantalla.fill((205, 144, 228))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            acaba = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicion_x_cambio = -0.1
                print('Flecha Izquierda <- Presionada')
            if evento.key == pygame.K_RIGHT:
                posicion_x_cambio = 0.1
                print('Flecha Derecha -> Presionada')

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or  evento.key == pygame.K_RIGHT:
                posicion_x_cambio = 0

    posicion_x += posicion_x_cambio
    jugador(posicion_x, posicion_y)

    pygame.display.update()