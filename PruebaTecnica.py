import pygame
import sys
import random
import time

#Nombre de la ventana
pygame.display.set_caption('ESQUIVA ESQUIVA')

#Constantes

Ancho = 800
Alto = 600
Color_rojo = (255,0,0)
Color_negro = (0,0,0)
Color_azul = (0,0,255)
Color_blanco = (255,255,255)

pygame.init()


#Jugador
Player_size = 50  #Tamaño
Player_pos = [Ancho / 2,Alto - Player_size * 2]

#Enemigo(s)
Enemy_size = 50  #Tamaño
Enemy_pos = [random.randint(0, Ancho - Enemy_size),0]

#Creacion de ventana de Juego
ventana = pygame.display.set_mode((Ancho,Alto))


#Generacion de reloj
clock = pygame.time.Clock()

#FUNCIONES:
#Funcion para mensajes en pantalla
font = pygame.font.SysFont(None, 25)
def message(msg, color):
    text = font.render(msg, True, color)
    ventana.blit(text, [Ancho/3, Alto/2])
def message1(msg, color):
    text = font.render(msg, True, color)
    ventana.blit(text, [Ancho/3, Alto/2.4])
def message2(msg, color):
    text = font.render(msg, True, color)
    ventana.blit(text, [Ancho/3, Alto/2.8])
    
#Funcion para colisiones
def detectar_colision(Player_pos, Enemy_pos):
    Px = Player_pos[0]
    Py = Player_pos[1]
    Ex = Enemy_pos[0]
    Ey = Enemy_pos[1]

    if (Ex >= Px and Ex <(Px + Player_size)) or (Px >= Ex and Px <(Ex + Enemy_size)):
        if (Ey >= Py and Ey <(Py + Player_size)) or (Py >= Ey and Py <(Ey + Enemy_size)):
            return True
    return False

#JUEGO
def Gamestart():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Movimiento del jugador
            if event.type == pygame.KEYDOWN:
                x = Player_pos[0]
                if event.key == pygame.K_LEFT:
                    x -= Player_size
                if event.key == pygame.K_RIGHT:
                    x += Player_size

                Player_pos[0] = x
        ventana.fill(Color_negro)

        #Creación de enemigos
        #Movimiento del enemigo
        if Enemy_pos[1] >= 0 and Enemy_pos[1] < Alto:
            Enemy_pos[1] += 20
        else:
            Enemy_pos[0] = random.randint(0, Ancho - Enemy_size)
            Enemy_pos[1] = 0

        pygame.draw.rect(ventana, Color_azul,
                        (Enemy_pos[0],Enemy_pos[1],
                        Enemy_size,Enemy_size))
        clock.tick(60)
        pygame.display.update()

        #Creación del jugador
        pygame.draw.rect(ventana, Color_rojo,
                        (Player_pos[0],Player_pos[1],
                        Player_size,Player_size))
        pygame.display.update()

        #Coliciones
        if detectar_colision(Player_pos, Enemy_pos):
            game_over = True
#MENU PRINCIPAL
game_start = False
while not game_start == True:
    message1("Presiona P para comenzar", Color_blanco)
    message("Presiona X para salir del juego", Color_blanco)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Gamestart()
            if event.key == pygame.K_x:
                 pygame.quit()










