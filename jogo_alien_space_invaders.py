import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

fonte_pixel_grande = pygame.font.Font("Minecraftia-Regular.ttf", 23)
fonte_pixel_micro = pygame.font.Font("Minecraftia-Regular.ttf", 20)

alien_img = pygame.image.load("alien.png").convert_alpha()
alien_img = pygame.transform.scale(alien_img, (int(474/10), int(353/10))) 

def criar_aliens():
    aliens = []
    for linha in range(3):  
        for coluna in range(8):
            x = 60 + coluna * 60 
            y = 60 + linha * 60  
            aliens.append((x, y))
    return aliens

def desenhar_aliens(tela, aliens):
    for alien in aliens:
        tela.blit(alien_img, (alien[0], alien[1]))

def jogo():
    tela_jogo = pygame.display.set_mode((640, 480))
    aliens = criar_aliens()
    rodando = True
    while rodando:
        tela_jogo.fill((0, 0, 0)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        desenhar_aliens(tela_jogo, aliens)
        pygame.display.flip()
        clock.tick(60)

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

    desenhar_texto("Derrote os aliens inimigos", fonte_pixel_grande, 50)
    desenhar_texto("antes que o tempo acabe", fonte_pixel_grande, 80)
    desenhar_texto("e vença o jogo!", fonte_pixel_grande, 107)
    desenhar_texto("Você está pronto(a) para a batalha?", fonte_pixel_grande, 350)
    desenhar_texto("Clique ENTER para começar o jogo", fonte_pixel_micro, 390)
    
    alien = pygame.image.load("alien.png").convert_alpha()
    alien = pygame.transform.scale(alien, (int(474/2.5), int(353/2.5)))
    x_centro = (640 // 2)-(alien.get_width() // 2)
    y_centro = (480 // 2)-(alien.get_height() // 2)
    screen.blit(alien, (x_centro, y_centro))

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    
