import pygame
import random
import time

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

tiro_img = pygame.image.load("tiro_nave.png").convert_alpha()
tiro_img = pygame.transform.scale(tiro_img, (int(30/6), int(85/6)))

tiros = []
bombas = []

def atirar(nave_x, nave_y):
    x = nave_x + nave_img.get_width() // 2 - tiro_img.get_width() // 2
    y = nave_y
    tiros.append([x, y])

def mover_tiros(tiros, aliens):
    for tiro in tiros[:]:
        tiro[1] -= 7  
        screen.blit(tiro_img, (tiro[0], tiro[1]))

        for alien in aliens[:]:
            if alien[0] < tiro[0] < alien[0] + alien_img.get_width() and \
               alien[1] < tiro[1] < alien[1] + alien_img.get_height():
                aliens.remove(alien)
                tiros.remove(tiro)
                break 
        if tiro[1] < 0:
            tiros.remove(tiro)

def desenhar_vidas(tela, vidas):
    for i in range(vidas):
        x = 10 + (i * 35)
        y = 10
        tela.blit(vidas_img, (x, y))

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

        bomba_rect = pygame.Rect(bomba[0], bomba[1], bombas_img.get_width(), bombas_img.get_height())
        nave_rect = pygame.Rect(nave_x, nave_y, nave_img.get_width(), nave_img.get_height())
        
        if bomba_rect.colliderect(nave_rect):  
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
        if limites[linha]:
            limite_direita = max(limites[linha]) + alien_img.get_width()
            limite_esquerda = min(limites[linha])
            if limite_direita >= 640 or limite_esquerda <= 0:
                direcoes[linha] *= -1
    return direcoes

def desenhar_texto(texto, fonte, y):
    surface_texto = fonte.render(texto, True, 'white')
    x = (640 // 2) - surface_texto.get_width() // 2
    screen.blit(surface_texto, (x, y))

def game_over():
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        reiniciar_jogo()
                        return
            screen.fill((0, 0, 0))

            desenhar_texto("Oh não!", fonte_pixel_grande, 70)
            desenhar_texto("Os aliens te derrotaram...", fonte_pixel_grande, 107)
            desenhar_texto("Quer jogar novamente?", fonte_pixel_grande, 350)
            desenhar_texto("Clique ENTER para recomeçar o jogo", fonte_pixel_micro, 390)

            alien = pygame.image.load("alien.png").convert_alpha()
            alien = pygame.transform.scale(alien, (int(474/2.5), int(353/2.5)))
            x_centro = (640 // 2)-(alien.get_width() // 2)
            y_centro = (480 // 2)-(alien.get_height() // 2)

            screen.blit(alien, (x_centro, y_centro))
            pygame.display.flip()
            clock.tick(60)

def tempo_esgotado():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reiniciar_jogo()
                    return
        screen.fill((0, 0, 0))
        desenhar_texto("Tempo esgotado!", fonte_pixel_grande, 70)
        desenhar_texto("Você não derrotou os aliens a tempo...", fonte_pixel_grande, 107)
        desenhar_texto("Quer jogar novamente?", fonte_pixel_grande, 350)
        desenhar_texto("Clique ENTER para recomeçar o jogo", fonte_pixel_micro, 390)

        alien = pygame.image.load("alien.png").convert_alpha()
        alien = pygame.transform.scale(alien, (int(474/2.5), int(353/2.5)))
        x_centro = (640 // 2)-(alien.get_width() // 2)
        y_centro = (480 // 2)-(alien.get_height() // 2)

        screen.blit(alien, (x_centro, y_centro))
        pygame.display.flip()
        clock.tick(60)

def reiniciar_jogo():
    global tiros, bombas, vidas
    tiros = []
    bombas = []
    vidas = 3
    jogo()

def jogo():
    aliens = criar_aliens()
    direcoes = {0: 1, 1: -1, 2: 1}
    nave_x = (640 // 2) - (nave_img.get_width() // 2)
    nave_y = 480 - nave_img.get_height() - 10
    vidas = 3
    rodando = True
    tempo_inicial = time.time()

    while rodando:
        screen.fill((0, 0, 0)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    atirar(nave_x, nave_y) 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nave_x > 0:
            nave_x -= 5  
        if keys[pygame.K_RIGHT] and nave_x < 640 - nave_img.get_width():
            nave_x += 5  

        direcoes = mover_aliens(aliens, direcoes)
        desenhar_aliens(screen, aliens)
        alien_atirar(aliens, bombas)
        mover_tiros(tiros, aliens)
        vidas = mover_bombas(bombas, nave_x, nave_y, vidas)
        desenhar_vidas(screen, vidas)
        screen.blit(nave_img, (nave_x, nave_y))

        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial
        if tempo_decorrido >= 20 or vidas <= 0:
            if tempo_decorrido >= 20:
                tempo_esgotado()  
            else:
                game_over()  
            rodando = False

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


    
