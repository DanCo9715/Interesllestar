import pygame

# Inicializar Pygame
pygame.init()

# Solicitar tamaño del agujero negro al usuario
peso = int(input('Ingresa el tamaño del agujero negro (en pixeles):  '))

# Ajustar el tamaño de la pantalla según el tamaño del agujero negro
ancho_pantalla = peso + 200
alto_pantalla = peso + 200
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Imagen Rotando')

# Cargar y redimensionar la imagen
imagen = pygame.image.load('BlackHole.jpeg')
imagen = pygame.transform.scale(imagen, (peso, peso))
rect = imagen.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2))

angulo = 0
reloj = pygame.time.Clock()

# Cargar y reproducir música
pygame.mixer.music.load('interstellar.mp3')
pygame.mixer.music.play(-1)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False  # Salir del bucle

    angulo -= 1  # Rota a la derecha
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    rect_rotado = imagen_rotada.get_rect(center=rect.center)

    screen.fill((50, 50, 100))
    screen.blit(imagen_rotada, rect_rotado.topleft)  # Ajustar la posición según sea necesario
    pygame.display.flip()
    reloj.tick(60)  # Limitar la tasa de fotogramas a 60 FPS

pygame.quit()
 