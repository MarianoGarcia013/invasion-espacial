import math

import  pygame
import  random

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

# Variables Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368 # ubicacion: ancho de pantalla/2 - tamaño del jugador/2 (64/2)
jugador_y = 536 # ubicacion para que el jugador toque el piso: pantalla(600)-tamaño del jugador(64)
jugador_x_cambio = 0

# Variables Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("nave-espacial.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# Variable de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0.3
bala_y_cambio = 50
bala_visible = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto)

# Agregar musica


# Texto final de juego
def texto_final():
    mi_fuente_final = fuente_final.render("JEUGO TERMINADO", True, (255,255,255))



#Funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo, (x,y))

# Funcion bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16,y+10))

# Funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return  True
    else:
        return False


# Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


# Loop del juego
se_ejecuta = True


while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))  # colocar la imagen de fondo

    # Iterar eventos
    for evento in pygame.event.get():

        # Iterar eventos
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(jugador_x, bala_y)

        # Evento soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicacion enemigo
    enemigo_x += enemigo_x_cambio



    # Mantener dentro de los bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Colision
    colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        print(colision + 1)

    enemigo(enemigo_x, enemigo_y)
    jugador(jugador_x, jugador_y)
    pygame.display.update()