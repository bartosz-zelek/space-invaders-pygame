import pygame

pygame.init()

class Ship(object):
    def __init__(self, x, y, width, height, ship_speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ship_speed = ship_speed
        self.ship_surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        self.ship_surface.blit(image, (0, 0))

    def draw(self, surface):
        ship_rect = self.ship_surface.get_rect(x=self.x, y=self.y)
        surface.blit(self.ship_surface, ship_rect)

    def move(self, surface, direction=1):
        self.x += self.ship_speed * direction
        if self.x+self.width >= surface.get_width():
            self.x = surface.get_width() - self.width
        if self.x <= 0:
            self.x = 0

    def in_surface(self, surface):
        pass


class Bullet(object):
    def __init__(self, x, y, width, height, speed, image):
        self.x = x
        self.y = y
        self.height = height
        self.speed = speed
        self.bullet_surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        self.bullet_surface.blit(image, (0, 0))

    def draw(self, surface):
        bullet_rect = self.bullet_surface.get_rect(x=self.x, y=self.y)
        surface.blit(self.bullet_surface, bullet_rect)

    def move(self, direction=1):
        self.y += self.speed * direction
