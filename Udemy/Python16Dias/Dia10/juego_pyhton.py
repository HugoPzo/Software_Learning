import pygame
import random
import math
# SONIDOS
from pygame import mixer

# INICIALIZAR PYGAME
pygame.init()

# CREAR PANTALLA - TAMAÑO PANTALLA - USAREMOS ESTE OBJETO PARA AGREGAR ELEMENTOS AL DISPLAY
pantalla = pygame.display.set_mode((700, 300))

clock = pygame.time.Clock()
dt = 0

# TITULO E ICONO --------------------------

# TITULO
pygame.display.set_caption("INVASION ESPACIAL")
# ICONO - 32px
icon = pygame.image.load("astronave.png")
pygame.display.set_icon(icon)
# FONDO
bg_image = pygame.image.load("fondo_espacio.png")

# AGREGAR MUSICA
# Cargar Musica
mixer.music.load("musica_fondo.mp3")
# Volumen Musica
mixer.music.set_volume(0.1)
# LOOP INFINITO - PLAY
mixer.music.play(-1)

# -----------------------------------------
mitad_display_x = (pygame.display.get_window_size()[0] // 2)

# JUGADOR ---------------------------------
# Jugador icono
nave_jugador = pygame.image.load("nave_jugador.png")
# Posicion jugador -  Mitad de pantalla
posicion_y_jugador = (pygame.display.get_window_size()[1]) - (nave_jugador.get_size()[1]) * 3
jugador_x =  mitad_display_x - (nave_jugador.get_size()[0] // 2)
jugador_y = posicion_y_jugador
player_speed = 10
puntaje = 0
# FUENTE PUNTAJE
fuente = pygame.font.Font("freesansbold.ttf", 15)
texto_x = 10
texto_y = 10

# FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    # Colocar tecto en pantalla
    # El antialiasing es una técnica que tiene como objetivo reducir las distorsiones y artefactos gráficos que aparecen en una imagen de alta resolución cuando esta se presenta a una resolución menor y viceversa (True)
    texto = fuente.render(f"PUNTAJE: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

posicion_borde_x = pygame.display.get_window_size()[0] - nave_jugador.get_size()[0]

# Colocamos al jugador en pantalla
def jugador(x, y): # Pasamos parametros dinamicos de posicion
    # Colocar jugador (imagen, posicion)
    pantalla.blit(nave_jugador, (x, y)) 


# MISIL JUGADOR -------------------------
imagen_misil = pygame.image.load("misil.png")
misil_x = 0
misil_y = posicion_y_jugador
misil_x_cambio = 0
misil_y_cambio = 6
misil_visible = False

# FUNCION MISIL JUGADOR
def misil(x, y):
    global misil_visible
    misil_visible = True
    pantalla.blit(imagen_misil, (x + (nave_jugador.get_size()[0] // 2) - 8, y - 10))
# -----------------------------------------

# ENEMIGO -------------------------------
nave_enemigo = pygame.image.load("nave_enemiga.png")
numero_naves_enemigas = 5
enemy_speed = 2

posicion_borde_enemigo_x = pygame.display.get_window_size()[0] - nave_enemigo.get_size()[0]

enemigo_x_cambio = enemy_speed
enemigo_y_cambio = 20


def posicion_enemigo():
    nave_enemigo_x = random.randint(0, posicion_borde_enemigo_x) 
    nave_enemigo_y = random.randint(0, (pygame.display.get_window_size()[1] // 2) - nave_enemigo.get_size()[1])

    return nave_enemigo_x, nave_enemigo_y

nave_enemigo_x, nave_enemigo_y = posicion_enemigo()

# COLOCAR ENEMIGO EN PANTALLA
def enemigo(x, y):
    pantalla.blit(nave_enemigo, (nave_enemigo_x, nave_enemigo_y))
    
# -----------------------------------------

# FUNCION DETECTAR COLISIONES
def hay_colision(x_1, y_1, x_2, y_2):
    # Formula distancia entre dos puntos
    distancia = math.sqrt((pow((x_2 - x_1), 2) + pow((y_2 - y_1), 2)))
    # CALCULAMOS LA DISTANCIA ENTRE OBJETOS, SI LA DISTANCIA ES MENOR A 27 ES MUY PROBABLE LA COLISION
    if distancia < 17:
        return True
    else:
        return False


# LOOP JUEGO - TODO LO QUE SE NECESITA ACTUALIZAR CONSTANTEMENTE IRA DENTRO DEL LOOP 
running = True
while running:

    # COLOR PANTALLA - RGB - TUPLA CON RGB - ANTES DE CUALQUIER EVENTO
    # pantalla.fill((00, 11, 28)) 
    pantalla.blit(bg_image, (0, 0))

    # PYGAME SE MANEJA POR EVENTOS
    for event in pygame.event.get():
        # SI SE DETECTA EL CIERRE DE LA VENTANA, EL PROGRAMA ACABA
        if event.type == pygame.QUIT:
            running = False

        # EVENTOS -----------------------------

        # EVENTO MOVIMIENTO CON TECLADO - AL MOMENTO DE PRESIONAR LA TECLA
        pressed = pygame.key.get_pressed()
        # MOVIMIENTOS POR TECLAS 'A' & 'D'
        if pressed[pygame.K_a]:
            jugador_x -= player_speed
            # jugador_x %= pygame.display.get_window_size()[0] - (nave_jugador.get_size()[0] // 2) # En caso de querer aparecer al otro lado de la pantalla
        elif pressed[pygame.K_d]:
            jugador_x += player_speed 
            # jugador_x %= pygame.display.get_window_size()[0] - (nave_jugador.get_size()[0] // 2)
        elif pressed[pygame.K_SPACE]:
            # CARGAMOS SONIDO - NO MUSICA
            sonido_misil = mixer.Sound("disparo.mp3")
            sonido_misil.set_volume(0.1)
            sonido_misil.play()
            # SOLO SE PUEDE DISPARAR SI EL MISIL NO ES VISIBLE
            if not misil_visible:
                misil_x = jugador_x
                misil_y = jugador_y
                misil(misil_x, misil_y)
                


        # EVENTO MOVIMIENTO CON TECLADO - AL MOMENTO DE LEVANTAR LA TECLA
        if event.type == pygame.KEYUP:
            # EVENTO DEJAR DE PRESIONAR A Y D
            if event.key == pygame.K_a or event.key == pygame.K_d:
                pass

    # ESTOS NO DEPENDEN DE EVENTOS, POR LO TANTO SE MOVERAN SIN UN EVENTO EN CURSO, NO INDENTAR

    # LIMITAR BORDES 
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= posicion_borde_x:
        jugador_x = posicion_borde_x


    # MOVIMIENTO ENEMIGO
    nave_enemigo_x += enemigo_x_cambio

    # LIMITAR BORDES ENEMIGO
    if nave_enemigo_x <= 0:
        enemigo_x_cambio = enemy_speed
        nave_enemigo_y += enemigo_y_cambio
    elif nave_enemigo_x >= posicion_borde_enemigo_x:
        enemigo_x_cambio = -enemy_speed
        nave_enemigo_y += enemigo_y_cambio

    # MOVIMIENTO MISIL
    if misil_y <= -imagen_misil.get_size()[1]:
        misil_y = jugador_y
        misil_visible = False

    if misil_visible:
        misil(misil_x, misil_y)
        misil_y -= misil_y_cambio

    # COLISION - MISIL -> ENEMIGO
    colision_misil = hay_colision(nave_enemigo_x, nave_enemigo_y, misil_x, misil_y)
    if colision_misil:
        sonido_colision = mixer.Sound("game_over.mp3")
        sonido_misil.set_volume(0.1)
        sonido_misil.play()
        misil_y = jugador_y
        misil_visible = False
        puntaje += 1
        nave_enemigo_x, nave_enemigo_y = posicion_enemigo()

    colision_jugador = hay_colision(jugador_x, jugador_y, nave_enemigo_x, nave_enemigo_y)
    if colision_jugador:
        print("Hola")

    # COLOCAMOS AL JUGADOR - LLAMAMOS FUNCION
    enemigo(nave_enemigo_x, nave_enemigo_y)
    jugador(jugador_x, jugador_y)
    
    # MOSTRAR PUNTAJE
    mostrar_puntaje(texto_x, texto_y)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # ACTUALIZAMOS EL DISPLAY CADA QUE HAGAMOS CAMBIOS
    pygame.display.update()

    


pygame.quit()