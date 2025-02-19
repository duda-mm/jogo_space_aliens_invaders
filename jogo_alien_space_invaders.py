#jogo space invaders

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def desenhar_texto(texto,fonte,y):
    surface_texto = fonte.render(texto, True, 'white')
    x = (640 // 2) - surface_texto.get_width() // 2

    screen.blit(surface_texto, (x, y))
fonte_grande = pygame.font.Font(None,35)
fonte_pequena = pygame.font.Font(None,33)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    desenhar_texto("Derrote os aliens inimigos",fonte_pequena,30)
    desenhar_texto("antes que o tempo acabe",fonte_pequena,60)
    desenhar_texto("e vença o jogo!",fonte_grande,87)

    alien = pygame.image.load()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    
