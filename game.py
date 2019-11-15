import pygame
from objects import Ship, Bullet
import random

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
bullet_image_down = pygame.transform.rotate(bullet_image_up, 180)
bullets = []
pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(1000, 2000))
ship_enemies = None
bullet_time = 0
enemy_move_time = 0
enemy_direction = 1
enemies_go_down = False


def redraw_window():
    window.blit(background_image, (0, 0))
    
def restart_game(text, color):
    global ship_enemies, ship, bullets
    font = pygame.font.SysFont('comicsans', 100)
    text = font.render(text, True, (255, 255, 255))
    window.blit(text, (screen_width/2-text.get_width()/2, screen_height/2))
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render('Naciśnij dowolny klawisz, aby rozpocząć nową grę...', True, color)
    window.blit(text, (screen_width/2-text.get_width()/2, screen_height/2+100))
    pygame.display.update()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                pause = False
                bullets = []
                ship_enemies = [[Ship(x*100+100, i*60, 64, 64, 15, enemy_image) for x in range(8)] for i in range(4)]
                ship.x = screen_width/2-ship.width/2

ship_enemies = [[Ship(x*100+100, i*60, 64, 64, 15, enemy_image) for x in range(8)] for i in range(4)]
while run:
    if not ship_enemies:
        restart_game('Wygrałeś!', (0, 255, 0))
        continue
    redraw_window()
    enemy_move_time += clock.get_rawtime()
    clock.tick(30)
    bullet_time += clock.get_rawtime()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT+1:
            ship_row = random.choice(ship_enemies)
            ship_enemy = random.choice(ship_row)
            bullets.append(Bullet(ship_enemy.x+ship_enemy.width/2, ship_enemy.y, 10, 26, 8, bullet_image_down))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move(-1)
    if keys[pygame.K_RIGHT]:
        ship.move(1)
    if keys[pygame.K_UP] and bullet_time/250 >= 1:
        bullet_time = 0
        bullets.append(Bullet(ship.x+ship.width/2, ship.y, 10, 26, -8, bullet_image_up))
    
    if ship.x+ship.width >= screen_width:
        ship.x = screen_width - ship.width
    if ship.x <= 0:
        ship.x = 0

    ship.draw(window)

    for bullet in bullets:
        if bullet.surface.get_rect(x=bullet.x, y=bullet.y).colliderect(ship.surface.get_rect(x=ship.x, y=ship.y)) and bullet.velocity > 0:
            bullets.pop(bullets.index(bullet))
            restart_game('Przegrałeś!', (255, 0, 0))
            continue
        for enemies_col in ship_enemies:
            if not enemies_col:
                ship_enemies.pop(ship_enemies.index(enemies_col))
            for ship_enemy in enemies_col:
                if bullet.surface.get_rect(x=bullet.x, y=bullet.y).colliderect(ship_enemy.surface.get_rect(x=ship_enemy.x, y=ship_enemy.y)) and bullet.velocity < 0:
                    try:
                        bullets.pop(bullets.index(bullet))
                        enemies_col.pop(enemies_col.index(ship_enemy))
                    except:
                        pass
        

        if bullet.y < -bullet.height or bullet.y > window.get_height():
            bullets.pop(bullets.index(bullet))
            continue
        bullet.move()
        bullet.draw(window)

    if enemies_go_down:
        enemies_go_down = False
        for enemies_col in ship_enemies:
            for ship_enemy in enemies_col:
                ship_enemy.move_down()

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
