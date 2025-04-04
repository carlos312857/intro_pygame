# Estructura de de un juego en pygame

## Inicilizaciòn  

- como en todo programa en python, se debe importar los modulos o librerias a utilizar 
`ìmport pygame`

- Inicializar pygame usando la funcion intt
(). Inicializa todos los modulos de pygame importados.
`pygame.init()`

## visualizacion de la ventana 

` ventana = pygame.display.set mode((600,400))`

-set_mode()es la funcion encargada de definir el tamaño de la ventana.En el ejemplo, se esta definiendo una ventana de 600 px de ancho , por 400 px de alto.

`` pygame.display.set_capcion("Mi ventana")``

- set_caption() es la funcuion que añade un titulo a la ventana 

## funcion set_mode()

``set_mode (size =(0,0),flags = 0, depth= o,display= 0)`

- size = ( 600,400):define el tamaño de la ventana.

-flags = define uno o mas comportamientos para la ventana.
      - Valores:
        -pygame.
        FULLSCREEN
        -pygame.RESIZABLE
    -ejemplo:
        -flags = pygame.FULLSCREEN | pygame.
        RESIZABLE: pantalla completa
        dimenciones modificables.

## Bucle del juago - game loop
- Bucle infinito que se interrumpira el cumplir ciertos criterios
- Reloj interno del juego 
- En cada interacion del bucle del juego podemos mover a un personaje , o tener en cuenta que un objeto ha alcanzado a otro o que se ha cruzado la linea de llegada, lo que quiere desir que la partida ha terminado.
- cada interacion es una oportunidad para actualizar todos los datos relacionados en el estado actual de la partida 
- en cada interacion se realiza las siguientes tareas:
     1. Comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle 
     2. actualizar los recursos necesarios para la interacion actual 
     3. obtener las entradas del sistema, o de interaccion con el juego
     4. actualizar todas las entidades que caracterizan el juego
     5. refrescar la pantalla 

## Superficies Pygame 
- Superficie:
  - elemento geometrico.
  - linea, poligono,imagen,texto que se muestran en la pantalla.
  - el poligono se puede o no rellenar de color 
  - las superficies se crean de diferente manera dependiendo del tiempo:
     - imagen: image.load()
     - texto: front.render()
     - superficie generica: pygame.surface()
     - ventana del juego: pygame.display.set_mode()
     
    
 # Ejemplo:Bandera de colombia 

  ```py
  # importamos la librerìa pygame
import pygame
import random 

# inicializamos los mòdulos de pygame
pygame.init()

#  Establecer tìtulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Colores de la bandera
amarillo = (255, 255, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)


# crear una superficie
superficie_amarillo = pygame.Surface((400,200))
superficie_azul = pygame.Surface((400, 100))
superficie_rojo = pygame.Surface((400, 100))




# Rellenamos la superficie de color amarillo, azul, rojo
superficie_amarillo.fill(amarillo)
superficie_azul.fill(azul)
superficie_rojo.fill(rojo)

# Inserto o muevo la superficie de la ventana 
ventana.blit(superficie_amarillo, (0,0))
ventana.blit(superficie_azul, (0,200))
ventana.blit(superficie_rojo, (0,300))



# Actualiza la visualizaciòn de la ventana 
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()pygame
```

!["bandera"](bandera%20colombia%2002.png)