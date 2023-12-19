import pygame
from pygame.sprite import Sprite


class SpaceShip(Sprite):
    def __init__(self, screen):
        """инициализация космического корабля"""
        super(SpaceShip, self).__init__()
        self.screen = screen
        self.screen_rectangle = screen.get_rect()
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rectangle.centerx
        self.center = float(self.rect.centerx)
        self.rect.centery = 675
        self.move_right = False
        self.move_left = False

    def output(self):
        """рисование космического корабля"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """обновление позиции космического корабля"""
        if self.move_right and self.rect.right < self.screen_rectangle.right:
            self.center += 8.5
        elif self.move_left and self.rect.left > 0:  # self.screen_rectangle.left:
            self.center -= 8.5
        self.rect.centerx = self.center

    def create_spaceship(self):
        """размещение космического корабля по центру внизу экрана"""
        self.center = self.screen_rectangle.centerx
