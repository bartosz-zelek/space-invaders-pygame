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
enemy_image = pygame.transform.scale(pygame.image.load('enemy.png'), (64, 64))
ship = Ship(screen_width/2-32, screen_height-64, 64, 64, 5, ship_image)
bullet_image_up = pygame.image.load('bullet.png')
bullets = []
ship_enemies = None
bullet_time = 0

def create_enemies(ship_enemies):
    pass

def redraw_window():
    window.blit(background_image, (0, 0))
    for bullet in bullets:
        if bullet.y < -bullet.height or bullet.y > window.get_height():
            bullets.pop(bullets.index(bullet))
            continue
        bullet.move(-1)
        bullet.draw(window)
    ship.draw(window)
    for enemies_col in ship_enemies:
        for ship_enemy in enemies_col:
            ship_enemy.draw(window)
    pygame.display.update()

ship_enemies = [[Ship(x*100+100, i*60, 64, 64, 4, enemy_image) for x in range(8)] for i in range(3)]
print(ship_enemies)
while run:
    clock.tick(30)
    bullet_time += clock.get_rawtime()
    redraw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move(window, -1)
    if keys[pygame.K_RIGHT]:
        ship.move(window)
    if keys[pygame.K_UP] and bullet_time/500 >= 1:
        bullet_time = 0
        bullets.append(Bullet(ship.x+ship.width/2, ship.y, 10, 26, 5, bullet_image_up))

pygame.quit()
