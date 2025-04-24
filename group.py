import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo con Group")

# Colores
AZUL = (0, 128, 255)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]: self.rect.x -= 5
        if teclas[pygame.K_RIGHT]: self.rect.x += 5
        if teclas[pygame.K_UP]: self.rect.y -= 5
        if teclas[pygame.K_DOWN]: self.rect.y += 5

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Crear instancias de los sprites
jugador = Jugador()
enemigos = pygame.sprite.Group()  # Grupo para los enemigos

# Añadir múltiples enemigos al grupo
for i in range(5):
    enemigo = Enemigo(100 * (i + 1), 100)
    enemigos.add(enemigo)

# Crear un grupo para todos los sprites (jugador + enemigos)
todos_los_sprites = pygame.sprite.Group(jugador, enemigos)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Actualizar todos los sprites
    todos_los_sprites.update()

    # Detectar colisiones entre el jugador y los enemigos
    colisiones = pygame.sprite.spritecollide(jugador, enemigos, False)
    if colisiones:
        print("¡Colisión con un enemigo!")

    # Dibujar todo en la pantalla
    pantalla.fill(BLANCO)
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización (FPS)
    reloj.tick(60)
