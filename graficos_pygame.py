import pygame
import sys 

rojo = (255,0,0)
azul = (0,0,255)

pygame.init()

ventana = pygame.display.set_mode((400,400))

pygame.display.set_caption("El cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3
##################
#bucle principal del juego
####################
while 1:
    clock.tick(50)
    # ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # si se hace click sobre boton de cerrar de la ventana, el juego termina 
        if event.type == pygame.QUIT:
            sys.exit()
    # rellenar la ventana de color 
    ventana.fill(azul)
    
    # dibujar formas con el modulo pygame.draw
   
    pygame.draw.line(ventana, rojo, (100,100),(300,300))
    pygame.draw.line(ventana, rojo, (100,300),(300,100))

    # dibujar una linea discontinua

    # actualiza la visualizacion de la ventana 
    pygame.display.flip()
######################################
# fin del bucleprincipal del juego 
######################################