import pygame

pygame.init()

peso = input('Ingresa tu peso: ')

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Imagen Rotando')

imagen = pygame.image.load('C:/Users/USER/desktop/BlackHole.jpeg')
# Use one load statement only
imagen = pygame.transform.scale(imagen, (400, 400))
rect = imagen.get_rect(center=(300, 200))

angulo = 0
reloj = pygame.time.Clock()

pygame.mixer.music.load('interstellar.mp3')
pygame.mixer.music.play(-1)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False  # Exit the loop

    angulo += 1
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    rect_rotado = imagen_rotada.get_rect(center=rect.center)

    screen.fill((255, 255, 255))
    screen.blit(imagen_rotada, rect_rotado.topright)
    pygame.display.flip()
    reloj.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
