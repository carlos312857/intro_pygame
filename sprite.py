import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo de Sprite con Colisión")

# Colores
AZUL = (0, 128, 255)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Clase Jugador que hereda de pygame.sprite.Sprite
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base Sprite
        self.image = pygame.Surface((50, 50))  # Crea una superficie rectangular
        self.image.fill(AZUL)  # Rellena la superficie con color azul
        self.rect = self.image.get_rect()  # Obtiene el rectángulo de la superficie
        self.rect.center = (400, 300)  # Establece la posición inicial del jugador

    def update(self):
        """Actualiza la posición del jugador según las teclas presionadas"""
        teclas = pygame.key.get_pressed()  # Detecta las teclas presionadas
        if teclas[pygame.K_LEFT]: self.rect.x -= 5  # Mover a la izquierda
        if teclas[pygame.K_RIGHT]: self.rect.x += 5  # Mover a la derecha
        if teclas[pygame.K_UP]: self.rect.y -= 5  # Mover hacia arriba
        if teclas[pygame.K_DOWN]: self.rect.y += 5  # Mover hacia abajo

# Clase Enemigo que también hereda de pygame.sprite.Sprite
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Superficie del enemigo
        self.image.fill(ROJO)  # Rellena con color rojo
        self.rect = self.image.get_rect()  # Rectángulo para colisiones
        self.rect.topleft = (x, y)  # Posición inicial del enemigo

# Crear las instancias de los sprites
jugador = Jugador()
enemigo = Enemigo(100, 100)

# Agrupar los sprites para actualizar y dibujar juntos
todos = pygame.sprite.Group(jugador, enemigo)

# Bucle principal del juego
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Cerrar el juego
            pygame.quit()
            exit()

    # Actualizar todos los sprites
    todos.update()

    # Detectar colisiones entre el jugador y el enemigo
    if pygame.sprite.spritecollideany(jugador, pygame.sprite.Group(enemigo)):
        print("¡Colisión con el enemigo!")

    # Dibujar todo en la pantalla
    pantalla.fill(BLANCO)  # Rellenar el fondo con blanco
    todos.draw(pantalla)  # Dibujar todos los sprites

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización (FPS)
    reloj.tick(60)
