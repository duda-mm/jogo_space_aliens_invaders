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
fonte_micro = pygame.font.Font(None,30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    desenhar_texto("Derrote os aliens inimigos",fonte_pequena,50)
    desenhar_texto("antes que o tempo acabe",fonte_pequena,80)
    desenhar_texto("e vença o jogo!",fonte_grande,107)
    desenhar_texto("Você está pronto(a) para a batalha?",fonte_grande,350)
    desenhar_texto("Clique ENTER para começar o jogo",fonte_micro,390)

    alien = pygame.image.load("alien.png").convert_alpha()
    alien = pygame.transform.scale(alien, (474//2.5,353//2.5))
    x_centro = (640//2)-(alien.get_width()//2)
    y_centro = (480//2)-(alien.get_height()//2)
    screen.blit(alien,(x_centro,y_centro))



    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    
