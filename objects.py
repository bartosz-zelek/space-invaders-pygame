import pygame

pygame.init()

class Ship(object):
    def __init__(self, x, y, width, height, ship_speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ship_speed = ship_speed
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        self.surface.blit(image, (0, 0))

    def draw(self, surface):
        ship_rect = self.surface.get_rect(x=self.x, y=self.y)
        surface.blit(self.surface, ship_rect)

    def move(self, direction=1):
        self.x += self.ship_speed * direction

    def move_down(self):
        self.y += self.ship_speed


class Bullet(object):
    def __init__(self, x, y, width, height, velocity, image):
        self.x = x
        self.y = y
        self.height = height
        self.velocity = velocity
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        self.surface.blit(image, (0, 0))

    def draw(self, surface):
        bullet_rect = self.surface.get_rect(x=self.x, y=self.y)
        surface.blit(self.surface, bullet_rect)

    def move(self):
        self.y += self.velocity
