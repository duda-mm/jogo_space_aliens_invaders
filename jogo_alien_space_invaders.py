import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

velocidade_aliens = 2.5

fonte_pixel_grande = pygame.font.Font("Minecraftia-Regular.ttf", 23)
fonte_pixel_micro = pygame.font.Font("Minecraftia-Regular.ttf", 20)

alien_img = pygame.image.load("alien.png").convert_alpha()
alien_img = pygame.transform.scale(alien_img, (int(474/12), int(353/12)))

nave_img = pygame.image.load("nave.png").convert_alpha()
nave_img = pygame.transform.scale(nave_img, (int(484/10), int(515/10)))

bombas_img = pygame.image.load("bomba.png").convert_alpha()
bombas_img = pygame.transform.scale(bombas_img, (int(499/12), int(499/12)))

vidas_img = pygame.image.load("vida.png").convert_alpha()
vidas_img = pygame.transform.scale(vidas_img, (int(360/12), int(360/12)))

def desenhar_vidas(tela, vidas):
    for i in range(vidas):
        x = 10 + (i * 35)
        y = 10
        tela.blit(vidas_img, (x, y))

bombas = []
def alien_atirar(aliens, bombas):
    if random.randint(0, 100) < 3.5: 
        alien_aleatorio = random.choice(aliens)
        x = alien_aleatorio[0] + alien_img.get_width() // 2
        y = alien_aleatorio[1] + alien_img.get_height()
        bombas.append([x, y])

def mover_bombas(bombas, nave_x, nave_y, vidas):
    for bomba in bombas[:]:
        bomba[1] += 5
        screen.blit(bombas_img, (bomba[0], bomba[1]))

        if (
            nave_x < bomba[0] < nave_x + nave_img.get_width()
            and nave_y < bomba[1] < nave_y + nave_img.get_height()
        ):
            vidas -= 1
            bombas.remove(bomba)
            if vidas <= 0:
                game_over() 
                return vidas
       
        elif bomba[1] > 480:
            bombas.remove(bomba)
    return vidas

def criar_aliens():
    aliens = []
    for linha in range(3):  
        for coluna in range(8):
            x = 50 + coluna * 60 
            y = 50 + linha * 60  
            aliens.append([x, y, linha])
    return aliens

def desenhar_aliens(tela, aliens):
    for alien in aliens:
        tela.blit(alien_img, (alien[0], alien[1]))

def mover_aliens(aliens, direcoes):
    for alien in aliens:
        linha = alien[2]
        alien[0] += direcoes[linha] * velocidade_aliens

    limites = {0: [], 1: [], 2: []}

    for alien in aliens:
        linha = alien[2]
        limites[linha].append(alien[0])

    for linha in range(3):
        limite_direita = max(limites[linha]) + alien_img.get_width()
        limite_esquerda = min(limites[linha])
        if limite_direita >= 640 or limite_esquerda <= 0:
            direcoes[linha] *= -1

    return direcoes

def game_over():
    game_over_screen = pygame.display.set_mode((640, 480))
    fonte = pygame.font.Font(None, 50)

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        jogo()
                        return

def jogo():
    aliens = criar_aliens()
    direcoes = {0: 1, 1: -1, 2: 1}
    nave_x = (640 // 2) - (nave_img.get_width() // 2)
    nave_y = 480 - nave_img.get_height() - 10
    vidas = 3
    rodando = True
    while rodando:
        screen.fill((0, 0, 0)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nave_x > 0:
            nave_x -= 5  
        if keys[pygame.K_RIGHT] and nave_x < 640 - nave_img.get_width():
            nave_x += 5  

        direcoes = mover_aliens(aliens, direcoes)
        desenhar_aliens(screen, aliens)
        alien_atirar(aliens, bombas)
        vidas = mover_bombas(bombas, nave_x, nave_y, vidas)
        desenhar_vidas(screen, vidas)
        screen.blit(nave_img, (nave_x, nave_y))
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
    desenhar_texto("Você está pronto (a) para a batalha?", fonte_pixel_grande, 350)
    desenhar_texto("Clique ENTER para começar o jogo", fonte_pixel_micro, 390)
    
    alien = pygame.image.load("alien.png").convert_alpha()
    alien = pygame.transform.scale(alien, (int(474/2.5), int(353/2.5)))
    x_centro = (640 // 2)-(alien.get_width() // 2)
    y_centro = (480 // 2)-(alien.get_height() // 2)
    screen.blit(alien, (x_centro, y_centro))

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    
