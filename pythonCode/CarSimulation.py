import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulación de Carreteras")

# Cargar imágenes de carros y carretera
car_image = pygame.image.load("car.png")  # Reemplaza "car.png" con la ruta de tu imagen de carro
car_image = pygame.transform.scale(car_image, (50, 80))  # Escalar la imagen del carro
road_image = pygame.image.load("road.jpg")  # Reemplaza "road.jpg" con la ruta de tu imagen de carretera
road_image = pygame.transform.scale(road_image, (screen_width, screen_height))

# Dibujar una franja blanca en la carretera
# pygame.draw.line(road_image, (255, 255, 255), (0, screen_height // 2), (screen_width, screen_height // 2), 5)

# Clase para representar un carro
class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1  # Velocidad del carro

    def update(self):
        self.rect.y += self.speed  # Mover hacia abajo

# Crear un grupo de sprites para los carros
all_sprites = pygame.sprite.Group()

# Crear carros y agregarlos al grupo de sprites
car1 = Car(car_image, 100, 100)
car2 = Car(car_image, 200, 200)
car3 = Car(car_image, 300, 300)
all_sprites.add(car1, car2, car3)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición de los carros
    all_sprites.update()

    # Dibujar el fondo de la carretera
    screen.blit(road_image, (0, 0))

    # Dibujar todos los sprites en la pantalla
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)
