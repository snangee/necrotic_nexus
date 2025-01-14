import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Necrotic Nexus')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, 'Green')
score_rect = score_surf.get_rect(center = (400,50))

aboba_surf = pygame.image.load('graphics/aboba.png').convert()
aboba_rect = aboba_surf.get_rect(bottomright = (600,150))

player_surf = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (300,250))

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos): print('coll')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('w')

        if event.type == pygame.KEYUP:
            print('UP')

    if game_active:

        screen.blit(ground_surface, (0, 0))
        screen.blit(score_surf, score_rect)

        aboba_rect.x -= 4
        if aboba_rect.right <=0: aboba_rect.left = 800

        screen.blit(aboba_surf, aboba_rect)
        screen.blit(player_surf, player_rect)

        #if player_rect.colliderect(aboba_rect):
        #    print('aboba')

        #keys = pygame.key.get_pressed()
        #keys[pygame.K_w]

        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        #if player_rect.collidepoint(mouse_pos):
        #    print(pygame.mouse.get_pressed())
        if player_rect.collidepoint(mouse_pos):
            if mouse_press[0]:
                game_active = False
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(30)