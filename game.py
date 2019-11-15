import pygame
from objects import Ship, Bullet

pygame.init()

run = True
clock = pygame.time.Clock()
screen_width, screen_height = (1000, 600)
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')
background_image = pygame.image.load('background.png')
ship_image = pygame.transform.scale(pygame.image.load('ship.png'), (64, 64))
enemy_image = pygame.transform.scale(pygame.image.load('enemy.png'), (64, 48))
ship = Ship(screen_width/2-32, screen_height-64, 64, 64, 5, ship_image)
bullet_image_up = pygame.image.load('bullet.png')
bullets = []
ship_enemies = None
bullet_time = 0
enemy_move_time = 0
enemy_direction = 1
enemies_go_down = False
enemies_went_down = []

def create_enemies(ship_enemies):
    pass

def redraw_window():
    window.blit(background_image, (0, 0))
    

ship_enemies = [[Ship(x*100+100, i*60, 64, 64, 10, enemy_image) for x in range(8)] for i in range(4)]
while run:
    redraw_window()
    enemy_move_time += clock.get_rawtime()
    clock.tick(30)
    bullet_time += clock.get_rawtime()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move(window, -1)
    if keys[pygame.K_RIGHT]:
        ship.move(window)
    if keys[pygame.K_UP] and bullet_time/250 >= 1:
        bullet_time = 0
        bullets.append(Bullet(ship.x+ship.width/2, ship.y, 10, 26, 8, bullet_image_up))
    
    if ship.x+ship.width >= screen_width:
        ship.x = screen_width - ship.width
    if ship.x <= 0:
        ship.x = 0

    ship.draw(window)

    for bullet in bullets:
        if bullet.y < -bullet.height or bullet.y > window.get_height():
            bullets.pop(bullets.index(bullet))
            continue
        bullet.move(-1)
        bullet.draw(window)

    if enemies_go_down:
        enemies_go_down = False
        enemies_went_down = []
        for enemies_col in ship_enemies:
            for ship_enemy in enemies_col:
                if ship_enemy not in enemies_went_down:
                    ship_enemy.move_down()
                    enemies_went_down.append(ship_enemy)

    for enemies_col in ship_enemies:
        for ship_enemy in enemies_col:
            if ship_enemy.x+ship_enemy.width >= screen_width:
                enemy_direction = -1
                ship_enemy.x -= 5
                enemies_go_down = True
            elif ship_enemy.x <= 0:
                enemy_direction = 1
                ship_enemy.x += 5
                enemies_go_down = True
            ship_enemy.draw(window)

            if enemy_move_time/250 >= 1:
                ship_enemy.move(enemy_direction)

    if enemy_move_time/250 >= 1:
        enemy_move_time = 0
        
    pygame.display.update()

pygame.quit()
