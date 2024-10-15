import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 675))
pygame.display.set_caption("Игра")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)


bg = pygame.image.load("background/icon.jpg").convert_alpha()

walk_right = [

pygame.image.load("images/player_right_stand.png").convert_alpha(),
pygame.image.load("images/player_right_walking.png").convert_alpha(),
pygame.image.load("images/player_right_walking2.png").convert_alpha(),

]

walk_left = [

pygame.image.load("images/player_left_stand.png").convert_alpha(),
pygame.image.load("images/player_left_walking.png").convert_alpha(),
pygame.image.load("images/player_left_walking2.png").convert_alpha(),
pygame.image.load("images/player_left_stand.png").convert_alpha()
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()

player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 150
player_y = 500

is_jump = False
jump_count = 8

label = pygame.font.Font('abc/Revoluzia.otf', 95)
lose_label = label.render('You lose!', False, (193, 196, 199))
restart_label = label.render('Try again', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(250, 350))

bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []
bullets_qual = 5

music = pygame.mixer.Sound('images/battle_2.mp3')
music.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)
ghost_list = []


gameplay = True
running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1200, 0))
    screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if ghost_list:
            for (i, el) in enumerate(ghost_list):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1100:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count >  0 :
                    player_y -= (jump_count  2) / 2
                else:
                    player_y += (jump_count  2) / 2
                jump_count -= 1

            else:
                is_jump = False
                jump_count = 8

        if player_anim_count == 2:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1200:
            bg_x = 0



        if bullets:
            for (i, el)  in enumerate(bullets):

                screen.blit(bullet,(el.x, el.y))
                el.x += 5
                if el.x > 1200:
                    bullets.pop(i)
                if ghost_list:
                    for (index, ghost_el) in enumerate(ghost_list):
                        if el.colliderect(ghost_el):
                            ghost_list.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label,(300,200))
        screen.blit(restart_label, restart_label_rect)
        bullets_qual = 5

    mouse = pygame.mouse.get_pos()
    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        player_x = 150
        ghost_list.clear()
        bullets.clear()
'hui'
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()