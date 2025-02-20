import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def jogo():
    tela_jogo = pygame.display.set_mode((640, 480))
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        
        tela_jogo.fill((0, 0, 0)) 
        pygame.display.flip()
    
    pygame.quit()
    exit()

def desenhar_texto(texto, fonte, y):
    surface_texto = fonte.render(texto, True, 'white')
    x = (640 // 2) - surface_texto.get_width() // 2
    screen.blit(surface_texto, (x, y))

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # K-RETURN -> ENTER
                jogo()
    
    screen.fill((0, 0, 0))
    fonte_pixel_grande = pygame.font.Font("Minecraftia-Regular.ttf", 23)
    fonte_pixel_micro = pygame.font.Font("Minecraftia-Regular.ttf", 20)

    desenhar_texto("Derrote os aliens inimigos", fonte_pixel_grande, 50)
    desenhar_texto("antes que o tempo acabe", fonte_pixel_grande, 80)
    desenhar_texto("e vença o jogo!", fonte_pixel_grande, 107)
    desenhar_texto("Você está pronto(a) para a batalha?", fonte_pixel_grande, 350)
    desenhar_texto("Clique ENTER para começar o jogo", fonte_pixel_micro, 390)
    
    alien = pygame.image.load("alien.png").convert_alpha()
    alien = pygame.transform.scale(alien, (int(474 / 2.5), int(353 / 2.5)))
    x_centro = (640 // 2) - (alien.get_width() // 2)
    y_centro = (480 // 2) - (alien.get_height() // 2)
    screen.blit(alien, (x_centro, y_centro))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    
